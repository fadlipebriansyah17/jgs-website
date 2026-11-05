// POST /api/admin/logout
import { clearSessionCookie } from "../../_lib/auth.js";
import { handle, json } from "../../_lib/http.js";

export const onRequestPost = handle(async ({ request }) => json({ ok: true }, 200, { "Set-Cookie": clearSessionCookie(request) }));
