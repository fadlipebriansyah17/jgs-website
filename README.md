# Website Resmi JAGARAYA GLOBAL SERVICES (JGS)

Website statis (HTML5, CSS3, JavaScript) tanpa framework. Enam halaman publik sudah selesai; Admin Panel masih placeholder.

| Halaman | File |
|---|---|
| Home | `public/index.html` |
| About Us | `public/about.html` |
| Our Services | `public/services.html` |
| Business Focus | `public/business-focus.html` |
| Our Clients | `public/clients.html` |
| Contact Us | `public/contact.html` |
| Admin (placeholder) | `public/admin/index.html` |

## Menjalankan di komputer

Folder `public/` adalah website final. Jalankan lewat server lokal:

```bash
cd public
python3 -m http.server 8000     # lalu buka http://localhost:8000
# atau: npx serve public
```

Membuka file HTML langsung (double-click) juga bisa, tetapi peta dan font Google butuh internet.

## Mengubah konten

Seluruh teks ada di `tools/content_id.py`. Setelah diubah, jalankan:

```bash
python3 tools/build.py      # menulis ulang semua file di public/*.html
```

Warna, font, dan jarak ada di `public/assets/css/tokens.css`. Kontak (alamat, telepon, WhatsApp) ada di bagian `SITE` pada `content_id.py`.

Mengganti foto: timpa file di `public/assets/images/<folder>/` dengan nama yang sama. Gambar saat ini diambil dari Company Profile JGS 2025 dan bersifat ilustrasi; sebagian berasal dari internet, sehingga sebaiknya diganti dokumentasi resmi sebelum publikasi.

## Catatan akurasi konten

- Tidak ada jumlah karyawan, jumlah klien, tahun berdiri, sertifikasi, penghargaan, atau statistik. Company Profile hanya memuat tangkapan layar dokumen tanpa keterangan, sehingga tidak ditampilkan sebagai sertifikasi.
- Logo klien (Mr. D.I.Y, J&T Express, ISTN) hanya yang tercantum di slide klien Company Profile. Mohon konfirmasi izin tampil. Slot lain adalah placeholder.
- Email perusahaan tidak dicantumkan karena tidak ada di dokumen.
- Salah ketik dikoreksi tanpa mengubah makna (mis. "Wasted" menjadi "Waste", "Isdustri" menjadi "industri").
- "Wastec International" disebut di profil dalam layanan pengolahan air limbah; mohon konfirmasi bentuk kerja samanya.

## Bahasa Inggris (nanti)

Salin `tools/content_id.py` menjadi `content_en.py`, terjemahkan nilainya, lalu daftarkan di `LANGS` pada `tools/build.py`. Teks UI JavaScript ada di `window.JGS.i18n` pada `assets/js/components.js`.

## Formulir kontak

Formulir sudah memiliki validasi. Pengiriman belum aktif: pengunjung diarahkan melanjutkan lewat WhatsApp dengan pesan terisi otomatis. Untuk mengaktifkan: buat D1, jalankan `migrations/0001_init.sql`, pasang binding `DB` di `wrangler.toml`, buka komentar kode di `functions/api/contact.js`, lalu isi `contactEndpoint` di `components.js`.

# Upload ke GitHub

```bash
cd jgs-website
git init
git add .
git commit -m "Website JGS: enam halaman publik"
git branch -M main
git remote add origin https://github.com/<akun>/<repo>.git
git push -u origin main
```

(Buat repo kosong terlebih dahulu di github.com.)

# Deploy ke Cloudflare Pages

1. Cloudflare Dashboard → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**, pilih repo.
2. Build command: kosongkan. **Build output directory: `public`**. Klik Deploy.
3. Domain: **Custom domains** → tambahkan `www.jagaraya.id` dan ikuti instruksi DNS.
4. Admin Panel nanti berada di `/admin` dan memakai Functions, D1, dan R2 (struktur `functions/`, `migrations/`, `wrangler.toml` sudah disiapkan).

Alternatif tanpa Git: `npx wrangler pages deploy public --project-name jgs-website`.
<!-- Trigger Cloudflare Pages deployment -->
