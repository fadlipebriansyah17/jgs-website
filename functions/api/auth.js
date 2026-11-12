// GET /api/auth — langkah 1 login Decap CMS dengan GitHub (OAuth).
// Decap membuka jendela popup ke alamat ini; kita arahkan pengguna ke halaman izin GitHub.
// Butuh variabel di Cloudflare Pages: GITHUB_CLIENT_ID dan GITHUB_CLIENT_SECRET (lihat docs/PANDUAN-AKTIVASI.md).
// Tidak ada database/R2: hanya meneruskan login. Hak menyimpan tetap ditentukan GitHub (akun harus punya akses tulis ke repo).

function randomHex(bytes) {
  const a = crypto.getRandomValues(new Uint8Array(bytes));
  return Array.from(a, (b) => b.toString(16).padStart(2, "0")).join("");
}

function errorPage(message, status) {
  const safe = String(message).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  return new Response(
    `<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Login Admin JGS</title>` +
      `<body style="font-family:system-ui,sans-serif;max-width:520px;margin:15vh auto;padding:0 20px;line-height:1.7;color:#102747">` +
      `<h2>Login belum bisa dilakukan</h2><p>${safe}</p><p style="color:#667">Tutup jendela ini dan hubungi pengelola website.</p>`,
    { status, headers: { "Content-Type": "text/html; charset=utf-8", "Cache-Control": "no-store" } }
  );
}

export async function onRequestGet({ request, env }) {
  if (!env.GITHUB_CLIENT_ID || !env.GITHUB_CLIENT_SECRET) {
    return errorPage("Pengaturan login GitHub belum lengkap: variabel GITHUB_CLIENT_ID dan GITHUB_CLIENT_SECRET belum diisi di Cloudflare Pages.", 503);
  }
  const url = new URL(request.url);
  const state = randomHex(16);
  const authorize = new URL("https://github.com/login/oauth/authorize");
  authorize.searchParams.set("client_id", env.GITHUB_CLIENT_ID);
  authorize.searchParams.set("redirect_uri", `${url.origin}/api/callback`);
  authorize.searchParams.set("scope", env.GITHUB_SCOPE || "public_repo"); // repo publik cukup 'public_repo'; ganti ke 'repo' bila repo dibuat privat
  authorize.searchParams.set("state", state);
  const secure = url.protocol === "https:" ? "; Secure" : "";
  return new Response(null, {
    status: 302,
    headers: {
      Location: authorize.toString(),
      "Set-Cookie": `jgs_oauth_state=${state}; Path=/api; HttpOnly; SameSite=Lax; Max-Age=600${secure}`,
      "Cache-Control": "no-store",
    },
  });
}
