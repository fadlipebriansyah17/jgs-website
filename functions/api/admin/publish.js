// POST /api/admin/publish — salin draft menjadi konten yang tampil di website publik.
import { requireAdmin } from "../../_lib/auth.js";
import { DEFAULT_CONTENT, sanitizeContent } from "../../_lib/content.js";
import { getDb, getDoc, putDoc } from "../../_lib/db.js";
import { handle, json } from "../../_lib/http.js";

export const onRequestPost = handle(async ({ env, request }) => {
  await requireAdmin(env, request);
  const db = await getDb(env);
  const draft = await getDoc(db, "draft");
  const clean = sanitizeContent(draft ? draft.content : DEFAULT_CONTENT);
  const at = await putDoc(db, "published", clean);
  return json({ ok: true, published_at: at });
});
