# Analisis Migrasi: CMS Kustom (D1/R2) → Decap CMS berbasis GitHub

## 1. Kondisi repository sebelum migrasi (hasil pemeriksaan file nyata)

- Website **statis** hasil generator Python: `tools/content_id.py` (data) + `tools/build.py` (templat) → `public/*.html`. `build.py` hanya memakai pustaka bawaan Python.
- Sebagian teks **tertanam di kode** `build.py` (judul hero Beranda, judul tiap bagian, catatan, deskripsi SEO, teks CTA/footer), sehingga tidak bisa diedit tanpa mengubah kode.
- `functions/api/contact.js` (kerangka, belum aktif), `migrations/0001_init.sql` (D1 untuk formulir kontak, belum dipakai), `wrangler.toml` (hanya nama, tanggal kompatibilitas, folder output).
- `build.py` menulis ulang `public/admin/index.html` (placeholder) setiap dijalankan → akan menimpa admin baru bila tidak dihentikan.
- CMS buatan sendiri (login password + D1 + R2) tidak pernah sampai ke produksi; deploy di Cloudflare tertinggal dari GitHub.
- Pengaturan Cloudflare Pages: Git-connected, build command kosong, output `public`, root kosong.

## 2. Pemilihan CMS

| Opsi | Penilaian |
|---|---|
| **Decap CMS** (dipilih) | Gratis dan open source; dashboard visual seperti contoh JRN Foundation (rute `#/collections/…/entries/…` adalah pola Decap); menyimpan konten & foto langsung ke GitHub; berjalan sebagai satu file JavaScript, tanpa server sendiri. |
| Sveltia CMS | Pengganti yang kompatibel dengan konfigurasi Decap, tampilan lebih modern, tetapi proyek lebih baru. Cadangan bila Decap kurang nyaman: cukup ganti satu baris di `public/admin/index.html`. |
| TinaCMS | Memerlukan layanan/backend tambahan; tidak sesuai syarat "tanpa layanan tambahan". |
| CMS kustom (D1/R2) | Membutuhkan D1, R2, kode login sendiri; pemeliharaan berat. Dinonaktifkan. |

## 3. Arsitektur baru

```
Admin (/admin/, Decap) ──login──► /api/auth → GitHub → /api/callback   (Pages Functions, gratis)
        │
        └─simpan──► GitHub API: commit ke main
                     • content/*.json  (teks)
                     • public/assets/images/uploads/*  (foto)
                              │
                              ▼
          Cloudflare Pages build:  python3 tools/build.py
                              │
                              ▼
          public/*.html (+ news.html, news/*.html)  → website publik
```

Konten admin **benar-benar terhubung** ke website: satu-satunya sumber teks adalah `content/*.json`, yang dibaca `build.py`. Tidak ada salinan konten kedua.

## 4. Daftar file

**Ditambah**
- `content/` — `site.json`, `home.json`, `about.json`, `services.json`, `business.json`, `clients.json`, `contact.json`, `news_page.json` (+ `news/*.json` saat ada berita)
- `public/admin/index.html` (pemuat Decap), `public/admin/config.yml` (struktur formulir admin)
- `functions/api/auth.js`, `functions/api/callback.js` (login GitHub)
- `public/_headers` (header keamanan untuk `/admin/*`)
- `docs/` (panduan), `_legacy-custom-cms/` (arsip)

**Diubah**
- `tools/content_id.py` → kini pemuat + pemeriksa file JSON (nama dan bentuk data yang dipakai `build.py` dipertahankan)
- `tools/build.py` → teks diambil dari JSON, jalur foto dari admin didukung, fitur berita, tidak lagi menulis `admin/index.html`
- `public/admin/dashboard.html` → pengalihan ke `/admin/`
- Stub 410 (nonaktif) pada `functions/api/admin/*`, `functions/api/content.js`, `functions/media/[[path]].js`
- `README.md`

**Dihapus oleh Anda (langkah manual)**: `wrangler.toml` (tidak dibutuhkan; bila ada, dashboard Cloudflare menjadi hanya-baca). Salinan di `_legacy-custom-cms/`.

**Tidak dipakai lagi (tidak dihapus, aman dibiarkan):** `public/assets/js/cms.js`, `functions/_lib/*` (bila ada), `tools/export_seed.py`, `migrations/0002_admin_cms.sql`, `SETUP-ADMIN.md` (bila ada). Boleh dihapus setelah admin stabil.

**Tidak diubah:** seluruh CSS, JS, gambar, struktur dan isi halaman publik (hasil build identik byte-per-byte dengan HTML sebelumnya).

## 5. Autentikasi GitHub di Cloudflare Pages

Decap di Netlify memakai Netlify Identity/Git Gateway; **di Cloudflare tidak tersedia**. Pengganti gratis: **GitHub OAuth App + dua Pages Function** (`/api/auth`, `/api/callback`).

- Diperlukan: OAuth App di GitHub (Client ID + Client Secret), callback `https://jgs-website.pages.dev/api/callback`.
- Variabel Cloudflare: `GITHUB_CLIENT_ID` (teks), `GITHUB_CLIENT_SECRET` (secret), opsional `ALLOWED_GITHUB_USERS`.
- Keamanan: `state` acak + cookie HttpOnly (anti-CSRF); rahasia klien hanya di server; token hanya dikirim ke jendela admin dengan alamat yang sama; izin `public_repo` (minimum untuk repo publik). **Hak menyimpan ditentukan GitHub**: hanya akun dengan akses tulis ke repo yang bisa mengubah apa pun. Tidak ada password admin yang disimpan di kode.
- Batasan: admin harus dibuka dari alamat yang sama dengan `base_url` di `config.yml` (saat ini `jgs-website.pages.dev`).
- Pengguna tambahan: tambahkan sebagai *Collaborator* (Write) di repo GitHub (gratis).

## 6. Biaya

GitHub (repo publik), Decap CMS, dan Cloudflare Pages paket gratis: Rp 0. Batas Pages gratis yang relevan: 500 build/bulan, 20.000 file/proyek, 25 MiB/file. Functions hanya terpakai saat login. Tiap simpan di admin = 1 build (unggah foto = commit tersendiri); pemakaian wajar jauh di bawah batas.

## 7. Risiko dan mitigasi

| Risiko | Mitigasi |
|---|---|
| File JSON salah → build gagal | `content_id.py` memeriksa dan menampilkan pesan jelas; build berhenti **sebelum** menulis apa pun, website live tetap utuh; Rollback tersedia di Cloudflare. |
| Python tidak tersedia di build Cloudflare | Image build v3 menyertakan Python 3.13; `build.py` tanpa pustaka luar; opsi `PYTHON_VERSION`. |
| Editor (unpkg.com) tidak termuat | Pesan jelas di `/admin/`; versi dapat dikunci ke nomor persis. |
| Admin mengubah "Kode tautan" layanan | Dilarang lewat petunjuk di formulir + validasi pola; id kembar ditolak saat build. |
| HTML di repo tertinggal dari konten | HTML dibangun ulang saat deploy; salinan repo sebagai cadangan yang identik dengan live saat migrasi. |
| Kuota 500 build/bulan | Edit banyak kolom, simpan sekali. |

## 8. Rencana bertahap dan rollback

1. Pindahkan konten ke JSON; **bukti:** HTML identik byte-per-byte. 2. Pasang Decap + login GitHub. 3. Tambah berita. 4. Nonaktifkan (bukan hapus) CMS lama. 5. Uji. 6. Aktivasi oleh pemilik (docs/PANDUAN-AKTIVASI.md).
Rollback: Cloudflare → Deployments → Rollback; atau revert commit di GitHub; kode lama ada di `_legacy-custom-cms/`.
