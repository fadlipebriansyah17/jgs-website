// Helper HTTP kecil untuk Pages Functions JGS.
export class HttpError extends Error {
  constructor(status, message, extra) { super(message); this.status = status; this.extra = extra || {}; }
}

export function json(data, status = 200, headers = {}) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store", ...headers },
  });
}

// Bungkus handler: ubah HttpError menjadi respons JSON yang rapi.
export function handle(fn) {
  return async (context) => {
    try {
      return await fn(context);
    } catch (err) {
      if (err instanceof HttpError) return json({ ok: false, error: err.message, ...err.extra }, err.status);
      console.error(err);
      return json({ ok: false, error: "Terjadi kesalahan pada server." }, 500);
    }
  };
}

export async function readJson(request, maxBytes = 1_000_000) {
  const text = await request.text();
  if (text.length > maxBytes) throw new HttpError(413, "Data terlalu besar.");
  try { return JSON.parse(text); } catch { throw new HttpError(400, "Format JSON tidak valid."); }
}
