// GET /api/admin/session — status login & kesiapan konfigurasi (dipakai layar login).
import { isAuthenticated, passwordConfigured } from "../../_lib/auth.js";
import { json, handle } from "../../_lib/http.js";

export const onRequestGet = handle(async ({ env, request }) => {
  return json({
    authenticated: await isAuthenticated(env, request),
    setup: { password: passwordConfigured(env), db: !!env.DB, media: !!env.MEDIA },
  });
});
