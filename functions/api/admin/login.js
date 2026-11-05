// POST /api/admin/login  { password }
import { getDb } from "../../_lib/db.js";
import { assertNotLocked, clearFails, clientIp, createSessionCookie, passwordMatches, recordFail } from "../../_lib/auth.js";
import { HttpError, handle, json, readJson } from "../../_lib/http.js";

export const onRequestPost = handle(async ({ env, request }) => {
  if (request.headers.get("X-Requested-With") !== "jgs-admin") throw new HttpError(403, "Permintaan ditolak.");
  const db = await getDb(env);
  const ip = clientIp(request);
  await assertNotLocked(db, ip);
  const body = await readJson(request, 2000);
  const ok = await passwordMatches(env, typeof body.password === "string" ? body.password : "");
  if (!ok) {
    await recordFail(db, ip);
    await new Promise((r) => setTimeout(r, 500));
    throw new HttpError(401, "Password salah.");
  }
  await clearFails(db, ip);
  return json({ ok: true }, 200, { "Set-Cookie": await createSessionCookie(env, request) });
});
