// Cloudflare Pages Function: POST /api/contact
// PLACEHOLDER — belum aktif. Setelah D1 dibuat dan binding "DB" terpasang di wrangler.toml,
// aktifkan penyimpanan pesan dengan membuka komentar di bawah dan isi
// `contactEndpoint: "/api/contact"` pada public/assets/js/components.js.
export async function onRequestPost(context) {
  // const body = await context.request.json();
  // await context.env.DB.prepare(
  //   "INSERT INTO contact_messages (name, company, phone, email, service, message) VALUES (?, ?, ?, ?, ?, ?)"
  // ).bind(body.name, body.company || null, body.phone, body.email, body.service || null, body.message).run();
  // return Response.json({ ok: true });

  return Response.json({ ok: false, error: "Pengiriman formulir belum diaktifkan." }, { status: 501 });
}
