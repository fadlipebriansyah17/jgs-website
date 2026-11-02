/* Komponen bersama JGS: konfigurasi situs + helper kecil.
   Dimuat sebelum main.js. Nantinya konfigurasi ini dapat diisi dari Admin Panel (D1). */
(function () {
  "use strict";

  window.JGS = window.JGS || {};

  window.JGS.config = {
    name: "JAGARAYA GLOBAL SERVICES",
    wa: "628161116375",
    phone: "+62 816 111 6375",
    lang: document.documentElement.lang || "id",
    // Diaktifkan setelah backend (Cloudflare Pages Functions + D1) tersedia.
    contactEndpoint: null, // contoh: "/api/contact"
  };

  /* Kamus teks untuk UI yang dibuat lewat JavaScript. Tambahkan "en" saat Bahasa Inggris disiapkan. */
  window.JGS.i18n = {
    id: {
      required: "Wajib diisi.",
      invalidEmail: "Format email tidak valid.",
      invalidPhone: "Masukkan nomor telepon yang valid (8–15 digit).",
      minMessage: "Pesan minimal 10 karakter.",
      consent: "Anda perlu menyetujui pernyataan ini.",
      pending: "Formulir sudah divalidasi. Pengiriman otomatis akan diaktifkan setelah backend tersedia. Sementara ini, silakan lanjutkan melalui WhatsApp dengan tombol di bawah.",
      waIntro: "Halo JGS, saya ingin berkonsultasi.",
    },
  };

  window.JGS.t = function (key) {
    var d = window.JGS.i18n[window.JGS.config.lang] || window.JGS.i18n.id;
    return d[key] || window.JGS.i18n.id[key] || key;
  };

  window.JGS.waLink = function (text) {
    return "https://wa.me/" + window.JGS.config.wa + (text ? "?text=" + encodeURIComponent(text) : "");
  };
})();
