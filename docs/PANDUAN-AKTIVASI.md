# Panduan Aktivasi Admin JGS (sekali saja, ±30 menit)

Admin JGS memakai **Decap CMS**. Semua teks dan foto disimpan di GitHub (repo `jgs-website`), lalu Cloudflare membangun ulang website otomatis. **Tanpa database, tanpa R2, tanpa biaya bulanan.**

Yang Anda butuhkan: akun GitHub pemilik repo `jgs-website` dan akun Cloudflare yang mengelola proyek `jgs-website`.

> Selama langkah-langkah ini belum selesai, **website publik tetap tampil seperti sekarang** (tidak ada yang berubah).

---

## Langkah 1 — Masukkan file ke GitHub

1. Ekstrak `jgs-decap-cms.zip` di komputer. Anda akan melihat folder `content`, `docs`, `functions`, `public`, `tools`, `_legacy-custom-cms` dan beberapa file.
2. Buka `github.com/fadlipebriansyah17/jgs-website` → klik **Add file → Upload files**.
3. **Seret semua folder dan file hasil ekstrak** ke kotak upload (bukan file ZIP-nya). Tunggu sampai semua terunggah.
4. Pada kotak "Commit changes" tulis `Pasang Admin Decap`, pilih **Commit directly to the main branch**, klik **Commit changes**.
5. **Hapus file `wrangler.toml`**: di halaman repo klik `wrangler.toml` → ikon tempat sampah (🗑) → **Commit changes**.
   (File ini sudah tidak dibutuhkan; kalau dibiarkan, pengaturan di Cloudflare menjadi terkunci. Salinannya aman di `_legacy-custom-cms/`.)
6. **Cek:** buka `github.com/fadlipebriansyah17/jgs-website/tree/main/content` → harus ada 8 file `.json`.

## Langkah 2 — Atur perintah build di Cloudflare

1. Buka dash.cloudflare.com → **Workers & Pages** → proyek **jgs-website** → **Settings** → **Builds** (atau *Build configuration*) → **Edit**.
2. Isi:
   - **Build command:** `python3 tools/build.py`
   - **Build output directory:** `public` (biarkan)
   - **Root directory:** kosong (biarkan)
3. **Save**.

## Langkah 3 — Buat "kunci login" GitHub (OAuth App)

1. Di GitHub: klik foto profil → **Settings** → (menu kiri paling bawah) **Developer settings** → **OAuth Apps** → **New OAuth App**.
2. Isi persis:
   - **Application name:** `JGS Admin`
   - **Homepage URL:** `https://jgs-website.pages.dev`
   - **Authorization callback URL:** `https://jgs-website.pages.dev/api/callback`
3. Klik **Register application**.
4. Salin **Client ID**. Lalu klik **Generate a new client secret** dan salin **Client secret** *saat itu juga* (hanya tampil sekali). Simpan keduanya sementara di Catatan.

## Langkah 4 — Masukkan kunci ke Cloudflare

1. Cloudflare → proyek **jgs-website** → **Settings** → **Variables and Secrets** (di versi lama: *Environment variables*) → **Add** (pastikan lingkungan **Production**).
2. Tambah dua isian:

   | Nama (persis) | Nilai | Jenis |
   |---|---|---|
   | `GITHUB_CLIENT_ID` | Client ID dari langkah 3 | Text |
   | `GITHUB_CLIENT_SECRET` | Client secret dari langkah 3 | **Secret** |

3. *(Opsional, lebih aman)* Tambah `ALLOWED_GITHUB_USERS` (Text) berisi nama akun GitHub yang boleh masuk, dipisah koma, mis. `fadlipebriansyah17,rekan-anda`.
4. **Save**.

## Langkah 5 — Deploy ulang

Cloudflare → **Deployments** → pada deployment paling atas klik **⋯ → Retry deployment** (atau cukup commit apa pun di GitHub). Tunggu status **Success** (1–3 menit).

## Langkah 6 — Coba

1. Buka `https://jgs-website.pages.dev/admin/` → klik **Login with GitHub** → **Authorize**.
2. Pilih **1. Beranda (Home)** → ubah satu kata → **Save/Publish**.
3. Tunggu 1–2 menit (Cloudflare membangun ulang), muat ulang website → perubahan tampil.

**Tanda berhasil sebelum login:** `https://jgs-website.pages.dev/admin/config.yml` menampilkan teks yang diawali `# Konfigurasi Admin Decap CMS`.

---

## Jika bermasalah

| Gejala | Penyebab & solusi |
|---|---|
| Deployment **Failed** | Buka "View build log". Pesan diawali `File konten ...` / `content/...` = ada file JSON salah (kirim pesannya). Pesan `python3: not found` = di Settings → Variables tambah `PYTHON_VERSION` = `3.11`. |
| Popup login: "Pengaturan login GitHub belum lengkap" | Langkah 4 belum benar (nama harus persis) atau belum deploy ulang (Langkah 5). |
| Popup: "Buka admin dari alamat yang sama…" | Admin dibuka dari alamat selain `jgs-website.pages.dev`. Buka lewat alamat itu. |
| Popup: "akun tidak termasuk daftar admin" | Tambahkan akun ke `ALLOWED_GITHUB_USERS`, atau hapus variabel itu. |
| Login berhasil tapi gagal menyimpan | Akun GitHub belum punya akses tulis. Repo → **Settings → Collaborators** → tambahkan akun (peran Write). |
| Admin kosong/putih | Browser memblokir pemuatan editor (unpkg.com). Matikan pemblokir iklan untuk situs ini atau coba browser lain. |
| Perubahan tidak muncul di website | Build command (Langkah 2) belum diisi, atau deployment masih berjalan. Cek **Deployments**. |

**Pemulihan cepat:** Cloudflare → **Deployments** → deployment lama yang baik → **⋯ → Rollback to this deployment**. Atau di GitHub, buka commit yang salah → **Revert**.

**Memakai domain `www.jagaraya.id` untuk admin?** Admin harus dibuka dari alamat yang sama dengan `base_url` di `public/admin/config.yml` dan *callback URL* di OAuth App. Saat ini keduanya `jgs-website.pages.dev`. Mengganti ke domain sendiri berarti mengubah ketiganya bersamaan.
