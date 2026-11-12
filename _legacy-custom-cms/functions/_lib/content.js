// Validasi & pembersihan konten dari dashboard. Semua teks diperlakukan sebagai teks biasa (bukan HTML).
import { HttpError } from "./http.js";
import { ICON_NAMES } from "./icons.js";
import { DEFAULT_CONTENT } from "./default-content.js";

export { DEFAULT_CONTENT };

const MODES = ["cover", "cutout", "contain"];
const LIMITS = { services: 20, sectors: 30, clients: 60, paras: 10, chips: 12, subs: 8, extra: 6, words: 8 };

const str = (v, max) => (typeof v === "string" ? v.replace(/\u0000/g, "").trim().slice(0, max) : "");
const arr = (v, max) => (Array.isArray(v) ? v.slice(0, max) : []);

// Gambar: '' (kosong), file bawaan (mis. services/cctv.jpeg), atau unggahan (/media/uploads/xxx.png).
export function cleanImg(v) {
  const s = str(v, 200);
  if (!s) return "";
  if (s.includes("..")) throw new HttpError(400, "Lokasi gambar tidak valid.");
  if (/^\/media\/uploads\/[A-Za-z0-9._-]+\.(png|jpe?g|webp|gif)$/i.test(s)) return s;
  if (/^[A-Za-z0-9_-]+(\/[A-Za-z0-9_.-]+)*\.(png|jpe?g|webp|gif)$/i.test(s)) return s;
  throw new HttpError(400, "Lokasi gambar tidak valid: " + s.slice(0, 60));
}
const cleanIcon = (v) => (ICON_NAMES.includes(v) ? v : "check");
const slug = (v) => str(v, 60).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");

export function sanitizeContent(input) {
  if (!input || typeof input !== "object") throw new HttpError(400, "Konten tidak valid.");
  const p = input.profile || {};
  const profile = {
    about: [str(arr(p.about, 2)[0], 3000), str(arr(p.about, 2)[1], 3000)],
    belief: str(p.belief, 3000),
    visi: str(p.visi, 1500),
    misi: str(p.misi, 1500),
    value: str(p.value, 1500),
    value_words: arr(p.value_words, LIMITS.words).map((w) => str(w, 40)).filter(Boolean),
    tata_nilai: str(p.tata_nilai, 3000),
    erp: str(p.erp, 3000),
  };

  const seen = new Set();
  const services = arr(input.services, LIMITS.services).map((s, i) => {
    s = s || {};
    const name = str(s.name, 120);
    if (!name) throw new HttpError(400, `Layanan nomor ${i + 1} belum diberi nama.`);
    let id = slug(s.id) || slug(name) || "layanan";
    let base = id, n = 2;
    while (seen.has(id)) id = base + "-" + n++;
    seen.add(id);
    return {
      id, name,
      icon: cleanIcon(s.icon),
      img: cleanImg(s.img),
      mode: MODES.includes(s.mode) ? s.mode : "cover",
      short: str(s.short, 500),
      long: arr(s.long, LIMITS.paras).map((x) => str(x, 3000)).filter(Boolean),
      chips: arr(s.chips, LIMITS.chips).map((x) => str(x, 60)).filter(Boolean),
      extra_imgs: arr(s.extra_imgs, LIMITS.extra).map(cleanImg).filter(Boolean),
      subs: arr(s.subs, LIMITS.subs).map((x) => ({ title: str(x && x.title, 120), text: str(x && x.text, 2000) })).filter((x) => x.title || x.text),
    };
  });

  const sectors = arr(input.sectors, LIMITS.sectors).map((s, i) => {
    s = s || {};
    const name = str(s.name, 120);
    if (!name) throw new HttpError(400, `Sektor nomor ${i + 1} belum diberi nama.`);
    return { name, desc: str(s.desc, 300), icon: cleanIcon(s.icon), img: cleanImg(s.img) };
  });

  const clients = arr(input.clients, LIMITS.clients).map((c, i) => {
    c = c || {};
    const name = str(c.name, 120);
    if (!name) throw new HttpError(400, `Klien nomor ${i + 1} belum diberi nama.`);
    return { name, img: cleanImg(c.img) };
  });

  let ph = parseInt(input.client_placeholders, 10);
  if (!Number.isFinite(ph)) ph = DEFAULT_CONTENT.client_placeholders;
  ph = Math.max(0, Math.min(ph, 12));

  return { profile, services, sectors, clients, client_placeholders: ph };
}

// Kumpulkan semua gambar unggahan yang dipakai (untuk mencegah penghapusan file yang sedang dipakai).
export function usedUploads(...docs) {
  const used = new Set();
  const walk = (v) => {
    if (typeof v === "string") { if (v.startsWith("/media/uploads/")) used.add(v); }
    else if (Array.isArray(v)) v.forEach(walk);
    else if (v && typeof v === "object") Object.values(v).forEach(walk);
  };
  docs.forEach(walk);
  return used;
}
