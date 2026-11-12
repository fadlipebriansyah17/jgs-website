# Website Resmi JAGARAYA GLOBAL SERVICES (JGS)

Website statis (HTML5, CSS3, JavaScript) tanpa framework. Enam halaman publik sudah selesai. Konten diedit lewat **Admin Decap CMS** di `/admin/` (login GitHub, tanpa database, tanpa biaya bulanan); panduan di folder `docs/`.

| Halaman | File |
|---|---|
| Home | `public/index.html` |
| About Us | `public/about.html` |
| Our Services | `public/services.html` |
| Business Focus | `public/business-focus.html` |
| Our Clients | `public/clients.html` |
| Contact Us | `public/contact.html` |
| Admin (Decap CMS) | `public/admin/index.html` + `public/admin/config.yml` |
| Berita & Aktivitas (otomatis, muncul setelah ada artikel) | `public/news.html`, `public/news/*.html` |

## Menjalankan di komputer

Folder `public/` adalah website final. Jalankan lewat server lokal:

```bash
cd public
python3 -m http.server 8000     # lalu buka http://localhost:8000
# atau: npx serve public
```

Membuka file HTML langsung (double-click) juga bisa, tetapi peta dan font Google butuh internet.

## Mengubah konten

**Cara utama: Admin Decap** di `https://jgs-website.pages.dev/admin/` (aktivasi: `docs/PANDUAN-AKTIVASI.md`, pemakaian: `docs/PANDUAN-ADMIN.md`).

Alur kerja: admin menyimpan → Decap membuat *commit* ke GitHub (`content/*.json`, foto di `public/assets/images/uploads/`) → Cloudflare Pages menjalankan `python3 tools/build.py` → halaman HTML diperbarui (1–2 menit).

| Isi | File data |
|---|---|
| Info perusahaan, kontak, ajakan, footer | `content/site.json` |
| Beranda / Tentang / Layanan / Fokus Bisnis / Klien / Kontak | `content/home.json`, `about.json`, `services.json`, `business.json`, `clients.json`, `contact.json` |
| Berita | `content/news/*.json` (1 file = 1 artikel), pengaturan halaman: `content/news_page.json` |

Mengedit manual tetap bisa: ubah file JSON lalu jalankan `python3 tools/build.py` (hanya butuh Python 3, tanpa pustaka tambahan). Jika ada file JSON yang salah, build berhenti dengan pesan jelas dan HTML yang ada tidak berubah.

Warna, font, dan jarak ada di `public/assets/css/tokens.css`.

Mengganti foto: lewat Admin (disarankan), atau timpa file di `public/assets/images/<folder>/`. Gambar saat ini diambil dari Company Profile JGS 2025 dan bersifat ilustrasi; sebagian berasal dari internet, sehingga sebaiknya diganti dokumentasi resmi sebelum publikasi.

> Catatan: file `public/*.html` di repo adalah hasil build. Setelah admin mengubah konten, Cloudflare membangun ulang HTML saat deploy; salinan di repo baru diperbarui bila `python3 tools/build.py` dijalankan lalu di-commit.

## Catatan akurasi konten

- Tidak ada jumlah karyawan, jumlah klien, tahun berdiri, sertifikasi, penghargaan, atau statistik. Company Profile hanya memuat tangkapan layar dokumen tanpa keterangan, sehingga tidak ditampilkan sebagai sertifikasi.
- Logo klien (Mr. D.I.Y, J&T Express, ISTN) hanya yang tercantum di slide klien Company Profile. Mohon konfirmasi izin tampil. Slot lain adalah placeholder.
- Email perusahaan tidak dicantumkan karena tidak ada di dokumen.
- Salah ketik dikoreksi tanpa mengubah makna (mis. "Wasted" menjadi "Waste", "Isdustri" menjadi "industri").
- "Wastec International" disebut di profil dalam layanan pengolahan air limbah; mohon konfirmasi bentuk kerja samanya.

## Bahasa Inggris (nanti)

Buat salinan folder `content/` untuk bahasa Inggris dan pemuat `content_en.py` (lihat `tools/content_id.py`), lalu daftarkan di `LANGS` pada `tools/build.py`. Teks UI JavaScript ada di `window.JGS.i18n` pada `assets/js/components.js`.

## Formulir kontak

Formulir sudah memiliki validasi. Pengiriman belum aktif: pengunjung diarahkan melanjutkan lewat WhatsApp dengan pesan terisi otomatis. Untuk mengaktifkan nanti (butuh D1): buat D1, jalankan `migrations/0001_init.sql`, buat `wrangler.toml` dengan binding `DB` (contoh di `_legacy-custom-cms/wrangler.toml.original`), buka komentar kode di `functions/api/contact.js`, lalu isi `contactEndpoint` di `components.js`.

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
2. **Build command: `python3 tools/build.py`**. **Build output directory: `public`**. Klik Deploy.
3. Domain: **Custom domains** → tambahkan `www.jagaraya.id` dan ikuti instruksi DNS.
4. Admin berada di `/admin/` (Decap CMS). Login memakai GitHub OAuth lewat Pages Functions `functions/api/auth.js` dan `callback.js`; variabel `GITHUB_CLIENT_ID` dan `GITHUB_CLIENT_SECRET` diatur di Cloudflare (lihat `docs/PANDUAN-AKTIVASI.md`).

CMS buatan sendiri sebelumnya (D1/R2) dinonaktifkan dan diarsipkan di `_legacy-custom-cms/`.
