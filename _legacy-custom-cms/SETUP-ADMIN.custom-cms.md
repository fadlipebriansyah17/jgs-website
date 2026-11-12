# Aktivasi Admin Dashboard JGS

## Mengapa dashboard belum tampil
1. File CMS belum ada di GitHub (`main` masih berisi dashboard lama).
2. Proyek Cloudflare Pages `jgs-website` tampaknya **tidak men-deploy otomatis dari GitHub** (versi live lebih tua dari isi GitHub), dan **upload drag-and-drop di dashboard Cloudflare tidak mendukung folder `functions/`**. Folder `functions/` hanya ikut ter-deploy lewat Git atau Wrangler.

## Langkah (berurutan)

### 1. Masukkan file ke proyek
Ekstrak `jgs-cms-upload.zip`. Salin **isinya** (folder `public`, `functions`, `tools`, `migrations`, dan `SETUP-ADMIN.md`) ke folder proyek `jgs-website`, timpa file lama. Jangan meng-upload file ZIP-nya sendiri.

Lalu ke GitHub: `git add -A`, `git commit -m "Tambah Admin Dashboard (CMS)"`, `git push`.
(Tanpa terminal: GitHub → **Add file → Upload files**, seret folder `public`, `functions`, `tools`, `migrations`, lalu Commit.)

Cek: `github.com/fadlipebriansyah17/jgs-website/tree/main/functions` harus berisi `_lib`, `api`, `media`.

### 2. Buat D1 dan R2
```bash
npx wrangler login
npx wrangler d1 create jgs-db
npx wrangler r2 bucket create jgs-media
```
Salin `database_id` dari perintah kedua. (R2 perlu diaktifkan dulu di Cloudflare Dashboard → R2.)

### 3. Edit `wrangler.toml` (file ini sengaja tidak ada di ZIP agar tidak menimpa edit Anda)
Tambahkan di bagian bawah:
```toml
[[d1_databases]]
binding = "DB"
database_name = "jgs-db"
database_id = "TEMPEL_DATABASE_ID_DI_SINI"

[[r2_buckets]]
binding = "MEDIA"
bucket_name = "jgs-media"
```
Nama binding harus persis `DB` dan `MEDIA`. Simpan, lalu commit/push lagi.

### 4. Set password admin
```bash
npx wrangler pages secret put ADMIN_PASSWORD --project-name jgs-website
```
(minimal 8 karakter)

### 5. Deploy dengan Wrangler (dari folder proyek yang berisi `functions/` dan `wrangler.toml`)
```bash
npx wrangler pages deploy --project-name jgs-website --branch main
```
Perintah ini yang membuat `functions/` ikut ter-deploy. Jika proyek Anda memang terhubung Git (Cloudflare → proyek → Deployments menampilkan commit GitHub), `git push` sudah cukup dan langkah ini opsional.

### 6. Pastikan
- `https://jgs-website.pages.dev/assets/js/cms.js` menampilkan **kode JavaScript** (bukan halaman beranda).
- `https://jgs-website.pages.dev/admin/` mengarah ke dashboard → layar login → masukkan password.

Pesan di layar login menunjukkan apa yang kurang: "Server API belum aktif" = langkah 5; "ADMIN_PASSWORD belum diatur" = langkah 4; "Database D1 belum terpasang" = langkah 2–3 lalu deploy ulang.

## Memakai
Edit → **Simpan Draft** (Ctrl+S) → **Publish**. Draft tidak tampil di website sebelum Publish.

## Keamanan & catatan
- Login satu password, sesi 8 jam, cookie `HttpOnly` + `SameSite=Strict`; 5 kali salah = blokir 15 menit per IP.
- Setelah Publish pertama, dashboard menjadi sumber konten utama; `tools/content_id.py` hanya cadangan.
- Hero, "Mengapa memilih JGS", kontak/alamat, dan footer belum bisa diedit dari dashboard.
