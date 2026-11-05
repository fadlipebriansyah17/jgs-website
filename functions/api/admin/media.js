// GET    /api/admin/media          — daftar foto yang diunggah
// POST   /api/admin/media          — unggah foto (multipart, field "file")
// DELETE /api/admin/media?key=...  — hapus foto (ditolak bila masih dipakai)
import { requireAdmin } from "../../_lib/auth.js";
import { usedUploads } from "../../_lib/content.js";
import { getDb, getDoc } from "../../_lib/db.js";
import { HttpError, handle, json } from "../../_lib/http.js";

const MAX_BYTES = 5 * 1024 * 1024;

function requireBucket(env) {
  if (!env.MEDIA) throw new HttpError(503, "Penyimpanan foto R2 belum terpasang. Ikuti langkah di SETUP-ADMIN.md (binding MEDIA).", { setup: "media" });
  return env.MEDIA;
}

// Tentukan tipe file dari isi file (bukan dari nama/ekstensi yang dikirim browser).
function sniff(b) {
  if (b.length > 12 && b[0] === 0x89 && b[1] === 0x50 && b[2] === 0x4e && b[3] === 0x47) return { ext: "png", type: "image/png" };
  if (b.length > 3 && b[0] === 0xff && b[1] === 0xd8 && b[2] === 0xff) return { ext: "jpg", type: "image/jpeg" };
  if (b.length > 6 && b[0] === 0x47 && b[1] === 0x49 && b[2] === 0x46 && b[3] === 0x38) return { ext: "gif", type: "image/gif" };
  if (b.length > 12 && b[0] === 0x52 && b[1] === 0x49 && b[2] === 0x46 && b[3] === 0x46 && b[8] === 0x57 && b[9] === 0x45 && b[10] === 0x42 && b[11] === 0x50) return { ext: "webp", type: "image/webp" };
  return null;
}

export const onRequestGet = handle(async ({ env, request }) => {
  await requireAdmin(env, request);
  const bucket = requireBucket(env);
  const list = await bucket.list({ prefix: "uploads/", limit: 1000 });
  const files = list.objects
    .map((o) => ({ key: o.key, url: "/media/" + o.key, size: o.size, uploaded: o.uploaded instanceof Date ? o.uploaded.toISOString() : String(o.uploaded) }))
    .sort((a, b) => (a.uploaded < b.uploaded ? 1 : -1));
  return json({ ok: true, files });
});

export const onRequestPost = handle(async ({ env, request }) => {
  await requireAdmin(env, request);
  const bucket = requireBucket(env);
  let form;
  try { form = await request.formData(); } catch { throw new HttpError(400, "Unggahan tidak valid."); }
  const file = form.get("file");
  if (!file || typeof file === "string") throw new HttpError(400, "Pilih file gambar terlebih dahulu.");
  if (file.size > MAX_BYTES) throw new HttpError(413, "Ukuran gambar maksimal 5 MB.");
  const bytes = new Uint8Array(await file.arrayBuffer());
  const kind = sniff(bytes);
  if (!kind) throw new HttpError(415, "Format tidak didukung. Gunakan PNG, JPG, WEBP, atau GIF.");
  const rand = crypto.getRandomValues(new Uint8Array(5)).reduce((s, b) => s + b.toString(16).padStart(2, "0"), "");
  const key = `uploads/${Date.now().toString(36)}-${rand}.${kind.ext}`;
  await bucket.put(key, bytes, {
    httpMetadata: { contentType: kind.type },
    customMetadata: { name: String(file.name || "").slice(0, 120) },
  });
  return json({ ok: true, key, url: "/media/" + key, size: bytes.length });
});

export const onRequestDelete = handle(async ({ env, request }) => {
  await requireAdmin(env, request);
  const bucket = requireBucket(env);
  const key = new URL(request.url).searchParams.get("key") || "";
  if (!/^uploads\/[A-Za-z0-9._-]+$/.test(key)) throw new HttpError(400, "Nama file tidak valid.");
  const db = await getDb(env);
  const draft = await getDoc(db, "draft");
  const published = await getDoc(db, "published");
  const used = usedUploads(draft && draft.content, published && published.content);
  if (used.has("/media/" + key)) throw new HttpError(409, "Foto ini masih dipakai di draft atau website publik. Ganti fotonya dulu, simpan/publish, lalu hapus.");
  await bucket.delete(key);
  return json({ ok: true });
});
