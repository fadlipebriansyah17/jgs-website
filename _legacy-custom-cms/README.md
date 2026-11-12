# Arsip CMS lama (tidak ikut di-deploy)

Folder ini menyimpan kode CMS buatan sendiri (D1 + R2 + login password) dan file asli sebelum migrasi ke Decap CMS.
Folder ini **tidak berada di `public/` atau `functions/`**, jadi tidak berjalan dan tidak dibaca Cloudflare.

Isi: kode API admin lama (`functions/`), dashboard lama, `cms.js`, skrip seed, migrasi D1 `0002`,
`content_id.original.py` + `build.original.py` (sumber konten lama berbasis Python), dan `wrangler.toml.original`.

Boleh dihapus kapan saja setelah Admin Decap berjalan stabil. Rollback penuh dimungkinkan lewat riwayat Git
(commit sebelum migrasi) atau dengan mengembalikan file-file di sini ke lokasi aslinya.
