// CMS lama (D1/R2) sudah DINONAKTIFKAN. Admin sekarang memakai Decap CMS di /admin/.
// Kode lama diarsipkan di _legacy-custom-cms/ (tidak dijalankan). File ini sengaja tanpa impor.
export function onRequest() {
  return new Response(JSON.stringify({ ok: false, error: "CMS lama sudah dinonaktifkan. Gunakan /admin/." }), {
    status: 410,
    headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" },
  });
}
