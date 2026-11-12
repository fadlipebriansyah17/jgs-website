// GET /api/callback — langkah 2 login Decap CMS dengan GitHub (OAuth).
// GitHub mengembalikan pengguna ke sini membawa "code". Kita tukar menjadi token (rahasia klien hanya ada di server),
// lalu menyerahkan token ke jendela Decap lewat postMessage. Token tidak disimpan di mana pun oleh server ini.
// Opsional: ALLOWED_GITHUB_USERS = "akun1,akun2" membatasi siapa yang boleh masuk (tambahan di atas izin tulis GitHub).

const enc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

function readCookie(request, name) {
  for (const part of (request.headers.get("Cookie") || "").split(";")) {
    const i = part.indexOf("=");
    if (i > 0 && part.slice(0, i).trim() === name) return part.slice(i + 1).trim();
  }
  return null;
}

function respond(status, message, content, secure) {
  // Halaman kecil yang berbicara dengan jendela Decap (pembuka popup) memakai protokol Decap/Netlify CMS.
  const payload = `authorization:github:${status}:${JSON.stringify(content)}`;
  const safeJson = JSON.stringify(payload).replace(/</g, "\\u003c");
  const body =
    `<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Login Admin JGS</title>` +
    `<body style="font-family:system-ui,sans-serif;max-width:520px;margin:15vh auto;padding:0 20px;line-height:1.7;color:#102747">` +
    `<p id="m">${enc(message)}</p>` +
    `<script>(function(){var msg=${safeJson};var me=window.location.origin;` +
    `if(!window.opener){document.getElementById("m").textContent="Jendela login ini harus dibuka dari halaman /admin/. Tutup jendela ini lalu mulai dari /admin/.";return;}` +
    `function receive(e){if(e.origin!==me){document.getElementById("m").textContent="Buka admin dari alamat yang sama dengan alamat login ("+me+"), lalu coba lagi.";return;}` +
    `window.removeEventListener("message",receive,false);window.opener.postMessage(msg,e.origin);}` +
    `window.addEventListener("message",receive,false);window.opener.postMessage("authorizing:github","*");})();</script>`;
  return new Response(body, {
    status: status === "success" ? 200 : 400,
    headers: {
      "Content-Type": "text/html; charset=utf-8",
      "Cache-Control": "no-store",
      "Referrer-Policy": "no-referrer",
      "Set-Cookie": `jgs_oauth_state=; Path=/api; HttpOnly; SameSite=Lax; Max-Age=0${secure ? "; Secure" : ""}`,
    },
  });
}

export async function onRequestGet({ request, env }) {
  const url = new URL(request.url);
  const secure = url.protocol === "https:";
  const fail = (m) => respond("error", m, { message: m }, secure);

  if (!env.GITHUB_CLIENT_ID || !env.GITHUB_CLIENT_SECRET) return fail("Pengaturan login GitHub belum lengkap di Cloudflare Pages.");
  if (url.searchParams.get("error")) return fail("Login dibatalkan atau ditolak di GitHub.");

  const code = url.searchParams.get("code");
  const state = url.searchParams.get("state");
  const saved = readCookie(request, "jgs_oauth_state");
  if (!code || !state || !saved || state !== saved) return fail("Sesi login tidak valid atau kedaluwarsa. Tutup jendela ini dan klik login lagi.");

  let token;
  try {
    const r = await fetch("https://github.com/login/oauth/access_token", {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json", "User-Agent": "jgs-decap-oauth" },
      body: JSON.stringify({ client_id: env.GITHUB_CLIENT_ID, client_secret: env.GITHUB_CLIENT_SECRET, code, redirect_uri: `${url.origin}/api/callback` }),
    });
    const data = await r.json();
    if (!data.access_token) return fail("GitHub menolak kode login" + (data.error_description ? ": " + data.error_description : "."));
    token = data.access_token;
  } catch (e) {
    return fail("Tidak dapat menghubungi GitHub. Coba lagi beberapa saat.");
  }

  const allowed = (env.ALLOWED_GITHUB_USERS || "").split(",").map((x) => x.trim().toLowerCase()).filter(Boolean);
  if (allowed.length) {
    try {
      const u = await fetch("https://api.github.com/user", { headers: { Authorization: `Bearer ${token}`, Accept: "application/vnd.github+json", "User-Agent": "jgs-decap-oauth" } });
      const login = u.ok ? String((await u.json()).login || "").toLowerCase() : "";
      if (!login || !allowed.includes(login)) return fail("Akun GitHub ini tidak termasuk daftar admin yang diizinkan.");
    } catch (e) {
      return fail("Tidak dapat memeriksa akun GitHub. Coba lagi.");
    }
  }
  return respond("success", "Login berhasil. Jendela ini akan tertutup otomatis…", { token, provider: "github" }, secure);
}
