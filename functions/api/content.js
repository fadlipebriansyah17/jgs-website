// GET /api/content  — konten yang sudah di-Publish (dibaca website publik).
import { getDb, getDoc } from "../_lib/db.js";
import { json, handle } from "../_lib/http.js";

export const onRequestGet = handle(async ({ env }) => {
  let doc = null;
  try {
    const db = await getDb(env);
    doc = await getDoc(db, "published");
  } catch {
    // D1 belum terpasang / error: website publik tetap memakai HTML bawaan.
    return json({ published: false }, 200, { "Cache-Control": "no-cache" });
  }
  if (!doc) return json({ published: false }, 200, { "Cache-Control": "no-cache" });
  return json({ published: true, updated_at: doc.updated_at, content: doc.content }, 200, { "Cache-Control": "no-cache" });
});
