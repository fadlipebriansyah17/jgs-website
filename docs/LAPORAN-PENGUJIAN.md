# Laporan Pengujian Migrasi Decap CMS

Pengujian dijalankan di lingkungan terisolasi (Python 3, Node 22, Chromium/Playwright) terhadap salinan repo JGS asli.

## Ringkasan

| Kelompok uji | Hasil |
|---|---|
| Build dari JSON vs HTML live asli (6 halaman) | **identik byte-per-byte** |
| Simulasi edit admin → build → HTML (teks, foto, layanan, sektor, klien, kontak, berita, keamanan teks, kegagalan aman) | **48/48 lulus** |
| Kecocokan kolom admin (`config.yml`) ↔ kunci/tipe data `content/*.json` | **282 nilai diperiksa, 0 masalah** |
| Login GitHub (`/api/auth`, `/api/callback`) — uji unit dengan GitHub tiruan | **26/26 lulus** |
| Browser nyata: alur popup login, serangan origin asing, loader admin, halaman berita (desktop + HP) | **27/27 lulus** |
| Uji tempel paket ke repo asli, dan ke repo "berantakan" (asli + paket CMS lama) | **6/6 halaman identik di keduanya; 48/48 dan 26/26 lulus** |

## Yang dibuktikan

1. **Desain & isi publik tidak berubah:** setelah konten dipindah ke JSON, `index`, `about`, `services`, `business-focus`, `clients`, `contact` identik byte-per-byte. Setelah berita ditambah lalu dihapus, kembali identik lagi.
2. **Admin benar-benar terhubung ke website:** mengubah JSON seperti yang dilakukan Decap mengubah HTML publik di semua tempat yang relevan (mis. nomor telepon/WhatsApp/alamat berubah di header, footer, dan halaman Kontak; layanan baru muncul di Beranda, halaman Layanan, indeks, dan pilihan formulir kontak).
3. **Foto unggahan tampil:** jalur `/assets/images/uploads/...` dari Decap dirender benar di halaman biasa dan halaman berita (`../`). Foto sektor dan logo klien opsional berfungsi.
4. **Aman terhadap teks berbahaya:** `<script>`, `<img onerror>`, tanda kutip, dan `&` di-escape di seluruh halaman.
5. **Kegagalan aman:** JSON rusak, file hilang, kolom wajib hilang, id layanan kembar, tanggal berita salah → build berhenti dengan pesan jelas dan **tidak mengubah satu pun file HTML**.
6. **Berita:** artikel draft tidak bocor; urutan terbaru→lama; tanggal berbahasa Indonesia; menu "Berita" otomatis muncul/hilang; halaman yang dihapus ikut hilang; tampilan responsif (tanpa scroll horizontal).
7. **Login:** state acak + cookie HttpOnly; kode ditukar di server dengan client secret (tidak pernah ke browser); sesi palsu/tanpa cookie ditolak; allowlist akun berfungsi; token berisi `</script>` tidak bisa keluar dari blok skrip; **halaman di origin lain yang membuka popup login tidak menerima token**.
8. **CMS lama dinonaktifkan:** 8 titik masuk lama menjawab 410; tidak ada route yang mengimpor file lain (build Cloudflare tidak bisa lagi gagal karena `_lib` hilang).

## Yang TIDAK bisa diuji di lingkungan ini (harus diverifikasi saat aktivasi)

| Hal | Alasan | Cara memverifikasi |
|---|---|---|
| Antarmuka Decap sungguhan | CDN unpkg tidak terjangkau dari lingkungan uji | Buka `/admin/`; `config.yml` sudah divalidasi YAML dan dicocokkan otomatis dengan data, tetapi belum dimuat oleh Decap itu sendiri |
| Login GitHub sungguhan | Perlu OAuth App milik Anda | Langkah 6 Panduan Aktivasi |
| Build Cloudflare (Python, bundling Functions) | Tidak ada akses ke Cloudflare | Status deployment **Success** + `/admin/config.yml` tampil |
| Commit Decap ke GitHub | Perlu token GitHub | Simpan satu perubahan uji lalu cek riwayat commit |

## Daftar periksa penggunaan pertama (±10 menit)

1. `https://jgs-website.pages.dev/admin/config.yml` tampil (bukan beranda).
2. `/admin/` → *Login with GitHub* → *Authorize* → daftar menu muncul di kiri.
3. Menu **1. Beranda** → ubah satu kata → *Save/Publish*.
4. GitHub → riwayat commit → ada commit baru "Konten: ubah beranda ...".
5. Cloudflare → Deployments → build baru **Success**; muat ulang website → perubahan tampil.
6. Unggah satu foto kecil di menu Klien/Layanan → tampil di halaman publik.
7. Buat satu berita uji → menu "Berita" muncul → matikan "Tampilkan di website" → menu hilang.
