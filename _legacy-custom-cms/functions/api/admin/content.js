// GET /api/admin/content  — draft (atau konten default bila belum pernah disimpan) + status
// PUT /api/admin/content  — simpan draft
import { requireAdmin } from "../../_lib/auth.js";
import { DEFAULT_CONTENT, sanitizeContent } from "../../_lib/content.js";
import { getDb, getDoc, putDoc } from "../../_lib/db.js";
import { handle, json, readJson } from "../../_lib/http.js";

const same = (a, b) => JSON.stringify(a) === JSON.stringify(b);

async function status(db) {
  const draft = await getDoc(db, "draft");
  const published = await getDoc(db, "published");
  const draftContent = draft ? draft.content : DEFAULT_CONTENT;
  const liveContent = published ? published.content : DEFAULT_CONTENT;
  return {
    draft_saved_at: draft ? draft.updated_at : null,
    published_at: published ? published.updated_at : null,
    unpublished: !same(draftContent, liveContent),
    content: draftContent,
  };
}

export const onRequestGet = handle(async ({ env, request }) => {
  await requireAdmin(env, request);
  const db = await getDb(env);
  return json({ ok: true, ...(await status(db)) });
});

export const onRequestPut = handle(async ({ env, request }) => {
  await requireAdmin(env, request);
  const db = await getDb(env);
  const clean = sanitizeContent(await readJson(request));
  await putDoc(db, "draft", clean);
  return json({ ok: true, ...(await status(db)) });
});
