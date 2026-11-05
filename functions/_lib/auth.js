// Login admin: satu password (secret ADMIN_PASSWORD), sesi cookie HttpOnly bertanda tangan HMAC.
import { HttpError } from "./http.js";

const COOKIE = "jgs_session";
const SESSION_SECONDS = 8 * 60 * 60;
const MAX_FAILS = 5;
const WINDOW_MS = 15 * 60 * 1000;
const enc = new TextEncoder();

function b64url(bytes) {
  let s = ""; bytes.forEach((b) => (s += String.fromCharCode(b)));
  return btoa(s).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}
function fromB64url(str) {
  str = str.replace(/-/g, "+").replace(/_/g, "/"); while (str.length % 4) str += "=";
  const bin = atob(str); return Uint8Array.from(bin, (c) => c.charCodeAt(0));
}

export function passwordConfigured(env) {
  return typeof env.ADMIN_PASSWORD === "string" && env.ADMIN_PASSWORD.length >= 8;
}

async function hmacKey(env) {
  if (!passwordConfigured(env)) {
    throw new HttpError(503, "ADMIN_PASSWORD belum diatur (minimal 8 karakter). Ikuti langkah di SETUP-ADMIN.md.", { setup: "password" });
  }
  const secret = env.SESSION_SECRET || "jgs-session|" + env.ADMIN_PASSWORD;
  return crypto.subtle.importKey("raw", enc.encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign", "verify"]);
}

async function sign(env, payload) {
  const key = await hmacKey(env);
  const sig = new Uint8Array(await crypto.subtle.sign("HMAC", key, enc.encode(payload)));
  return b64url(sig);
}

// Bandingkan password tanpa membocorkan panjang/isi lewat waktu respons.
export async function passwordMatches(env, candidate) {
  const key = await hmacKey(env);
  const a = new Uint8Array(await crypto.subtle.sign("HMAC", key, enc.encode(String(candidate))));
  const b = new Uint8Array(await crypto.subtle.sign("HMAC", key, enc.encode(env.ADMIN_PASSWORD)));
  let diff = 0; for (let i = 0; i < a.length; i++) diff |= a[i] ^ b[i];
  return diff === 0;
}

export async function createSessionCookie(env, request) {
  const payload = b64url(enc.encode(JSON.stringify({ exp: Math.floor(Date.now() / 1000) + SESSION_SECONDS })));
  const token = payload + "." + (await sign(env, payload));
  const secure = new URL(request.url).protocol === "https:" ? "; Secure" : "";
  return `${COOKIE}=${token}; Path=/; HttpOnly; SameSite=Strict; Max-Age=${SESSION_SECONDS}${secure}`;
}

export function clearSessionCookie(request) {
  const secure = new URL(request.url).protocol === "https:" ? "; Secure" : "";
  return `${COOKIE}=; Path=/; HttpOnly; SameSite=Strict; Max-Age=0${secure}`;
}

function readCookie(request, name) {
  const header = request.headers.get("Cookie") || "";
  for (const part of header.split(";")) {
    const i = part.indexOf("=");
    if (i > 0 && part.slice(0, i).trim() === name) return part.slice(i + 1).trim();
  }
  return null;
}

export async function isAuthenticated(env, request) {
  if (!passwordConfigured(env)) return false;
  const token = readCookie(request, COOKIE);
  if (!token || !token.includes(".")) return false;
  const [payload, sig] = token.split(".");
  try {
    const key = await hmacKey(env);
    const ok = await crypto.subtle.verify("HMAC", key, fromB64url(sig), enc.encode(payload));
    if (!ok) return false;
    const { exp } = JSON.parse(new TextDecoder().decode(fromB64url(payload)));
    return typeof exp === "number" && exp > Date.now() / 1000;
  } catch { return false; }
}

// Wajib login; untuk method yang mengubah data, wajib header X-Requested-With (perlindungan CSRF tambahan).
export async function requireAdmin(env, request) {
  if (!(await isAuthenticated(env, request))) throw new HttpError(401, "Sesi berakhir. Silakan login kembali.");
  if (!["GET", "HEAD"].includes(request.method) && request.headers.get("X-Requested-With") !== "jgs-admin") {
    throw new HttpError(403, "Permintaan ditolak.");
  }
}

// ---- Pembatasan percobaan login (5 gagal / 15 menit per IP) ----
export function clientIp(request) {
  return request.headers.get("CF-Connecting-IP") || request.headers.get("X-Forwarded-For") || "local";
}
export async function assertNotLocked(db, ip) {
  const row = await db.prepare("SELECT count, first_at FROM login_fail WHERE ip = ?").bind(ip).first();
  if (row && row.count >= MAX_FAILS && Date.now() - row.first_at < WINDOW_MS) {
    const minutes = Math.ceil((WINDOW_MS - (Date.now() - row.first_at)) / 60000);
    throw new HttpError(429, `Terlalu banyak percobaan. Coba lagi dalam ${minutes} menit.`);
  }
}
export async function recordFail(db, ip) {
  const now = Date.now();
  const row = await db.prepare("SELECT count, first_at FROM login_fail WHERE ip = ?").bind(ip).first();
  if (!row || now - row.first_at >= WINDOW_MS) {
    await db.prepare("INSERT INTO login_fail (ip, count, first_at) VALUES (?, 1, ?) ON CONFLICT(ip) DO UPDATE SET count = 1, first_at = excluded.first_at").bind(ip, now).run();
  } else {
    await db.prepare("UPDATE login_fail SET count = count + 1 WHERE ip = ?").bind(ip).run();
  }
}
export async function clearFails(db, ip) {
  await db.prepare("DELETE FROM login_fail WHERE ip = ?").bind(ip).run();
}
