# Cara Memakai Admin JGS

Alamat: **https://jgs-website.pages.dev/admin/** → **Login with GitHub**.

## Menu di sisi kiri

| Menu | Isinya |
|---|---|
| 1. Beranda (Home) | Judul utama, profil singkat, keunggulan, teks tiap bagian di Beranda |
| 2. Tentang Kami | Profil, visi, misi, value, tata nilai, ERP |
| 3. Layanan (Services) | Tambah/ubah/urutkan layanan, foto, sub-layanan |
| 4. Fokus Bisnis | Sektor yang dilayani (boleh diberi foto) dan nilai tambah |
| 5. Klien | Nama dan logo klien |
| 6. Kontak & Info Perusahaan | Alamat, telepon, WhatsApp, teks halaman Kontak, ajakan dan footer |
| Berita & Aktivitas | Artikel berita (tombol **New Berita**) |
| 8. Pengaturan Halaman Berita | Judul halaman berita |
| **Media** (atas) | Semua foto yang pernah diunggah |

## Mengubah teks
Pilih menu → pilih halaman → ubah → **Save** / **Publish** (kanan atas). Tunggu **1–2 menit**, lalu muat ulang website.

## Mengganti/menambah foto
Klik kolom foto → **Choose an image** → **Upload** (pilih file) atau pilih dari daftar → **Save**.
Foto tersimpan di GitHub (`public/assets/images/uploads/`). Disarankan **di bawah 1 MB** (JPG/WEBP) agar website cepat.

## Mengelola daftar (layanan, sektor, klien)
- **Add** menambah item, tarik ikon ⋮⋮ untuk mengurutkan, ikon sampah untuk menghapus.
- Layanan baru: isi **Kode tautan** (huruf kecil/angka/tanda minus, mis. `fasilitas-baru`). **Jangan ubah kode layanan yang sudah ada** — tautan lama akan putus.
- Klien: kosongkan logo bila belum ada; atur "Jumlah kotak kosong" di menu Klien.

## Berita
**Berita & Aktivitas → New Berita** → isi judul, tanggal, isi (pisahkan paragraf dengan baris kosong), foto sampul (opsional) → **Publish**.
Menu **Berita** muncul otomatis di website setelah ada artikel. Matikan **Tampilkan di website** untuk menyembunyikan tanpa menghapus.

## Catatan penting
- Setiap penyimpanan = 1 perubahan di GitHub dan 1 pembangunan ulang. Paket gratis Cloudflare: 500 pembangunan/bulan → ubah beberapa kolom sekaligus, lalu simpan sekali.
- Teks ditulis sebagai **teks biasa** (tanpa HTML).
- Salah simpan? Pulihkan lewat riwayat commit di GitHub atau *Rollback* di Cloudflare (lihat Panduan Aktivasi).
