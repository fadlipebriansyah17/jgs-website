// GET /media/uploads/<file>  — menyajikan foto dari R2 (publik, hanya folder uploads/).
export async function onRequestGet({ env, params }) {
  const key = Array.isArray(params.path) ? params.path.join("/") : String(params.path || "");
  if (!env.MEDIA || !/^uploads\/[A-Za-z0-9._-]+$/.test(key)) return new Response("Not found", { status: 404 });
  const obj = await env.MEDIA.get(key);
  if (!obj) return new Response("Not found", { status: 404 });
  const headers = new Headers();
  headers.set("Content-Type", (obj.httpMetadata && obj.httpMetadata.contentType) || "application/octet-stream");
  headers.set("Cache-Control", "public, max-age=31536000, immutable");
  headers.set("X-Content-Type-Options", "nosniff");
  if (obj.httpEtag) headers.set("ETag", obj.httpEtag);
  return new Response(obj.body, { headers });
}
