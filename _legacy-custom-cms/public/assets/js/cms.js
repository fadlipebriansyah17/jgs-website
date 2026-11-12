/* JGS CMS (publik): menampilkan konten yang di-Publish dari Admin Dashboard.
   Template di bawah meniru markup tools/build.py, sehingga tampilan website tidak berubah.
   Jika belum ada konten yang dipublish (atau API gagal), HTML bawaan tetap dipakai. */
(function () {
  "use strict";
  var ICONS = {"shield": "M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z|M9 12l2 2 4-4", "sparkle": "M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z|M19 3v4|M17 5h4", "users": "M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2|M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z|M22 21v-2a4 4 0 0 0-3-3.9|M16 3.1a4 4 0 0 1 0 7.8", "parking": "M4 4h16v16H4z|M9 17V7h4a3 3 0 0 1 0 6H9", "bug": "M8 8h8v7a4 4 0 0 1-8 0z|M9 5l1.5 2|M15 5l-1.5 2|M3 10h5|M16 10h5|M3 18l5-2|M21 18l-5-2|M12 8v11", "camera": "M3 7h4l2-3h6l2 3h4v13H3z|M12 17a4 4 0 1 0 0-8 4 4 0 0 0 0 8z", "truck": "M2 6h11v10H2z|M13 9h4l4 4v3h-8z|M7 19a2 2 0 1 0 0-4 2 2 0 0 0 0 4z|M17 19a2 2 0 1 0 0-4 2 2 0 0 0 0 4z", "leaf": "M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z|M2 21c0-3 1.9-5.5 6-7", "building": "M4 21V4h10v17|M14 9h6v12|M8 8h2|M8 12h2|M8 16h2|M2 21h20", "bank": "M3 10l9-6 9 6|M5 10v8|M9 10v8|M15 10v8|M19 10v8|M3 21h18", "factory": "M2 21V10l6 4v-4l6 4v-4l6 4v7z|M17 3v7|M2 21h20", "box": "M21 8l-9-5-9 5v8l9 5 9-5z|M3 8l9 5 9-5|M12 13v8", "hospital": "M4 21V5h16v16|M12 9v6|M9 12h6|M2 21h20", "home": "M3 11l9-8 9 8|M5 10v11h14V10|M10 21v-6h4v6", "bed": "M3 18V6|M3 14h18v4|M21 14v-2a3 3 0 0 0-3-3h-7v5|M7.5 11.5h.01", "bag": "M5 8h14l-1 13H6z|M9 8V6a3 3 0 0 1 6 0v2", "cap": "M2 9l10-5 10 5-10 5z|M6 11.5V16c0 1.5 3 3 6 3s6-1.5 6-3v-4.5|M22 9v6", "check": "M5 12l5 5 9-10", "phone": "M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z", "pin": "M12 22s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z|M12 12a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z", "chat": "M21 12a8 8 0 0 1-11.7 7L3 21l2-5.5A8 8 0 1 1 21 12z", "arrow": "M5 12h14|M13 6l6 6-6 6", "target": "M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20z|M12 18a6 6 0 1 0 0-12 6 6 0 0 0 0 12z|M12 14a2 2 0 1 0 0-4 2 2 0 0 0 0 4z", "eye": "M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z|M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z", "flag": "M5 21V4|M5 4h13l-2 4 2 4H5", "heart": "M12 20s-8-5-8-11a4.5 4.5 0 0 1 8-2.5A4.5 4.5 0 0 1 20 9c0 6-8 11-8 11z", "layers": "M12 3l9 5-9 5-9-5z|M3 13l9 5 9-5", "chart": "M4 20V4|M4 20h16|M8 16v-4|M12 16V8|M16 16v-6", "doc": "M6 3h9l4 4v14H6z|M14 3v5h5|M9 13h6|M9 17h6", "cog": "M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z|M12 2v3|M12 19v3|M2 12h3|M19 12h3|M5 5l2 2|M17 17l2 2|M19 5l-2 2|M7 17l-2 2", "server": "M3 4h18v6H3z|M3 14h18v6H3z|M7 7h.01|M7 17h.01", "image": "M3 4h18v16H3z|M3 16l5-5 4 4 3-3 6 6|M9 9h.01", "plus": "M12 5v14|M5 12h14"};

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#x27;" }[c];
    });
  }
  function icon(name) {
    var d = ICONS[name] || ICONS.check;
    return '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true">' +
      d.split("|").map(function (p) { return '<path d="' + p + '"/>'; }).join("") + "</svg>";
  }
  function src(p) { return /^(\/|https?:\/\/)/.test(p) ? p : "assets/images/" + p; }
  function img(path, alt) {
    return path ? '<img src="' + esc(src(path)) + '" alt="' + esc(alt) + '" loading="lazy">' : "";
  }
  function $(s, c) { return (c || document).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  function reveal(root) { $$(".reveal", root).forEach(function (el) { el.classList.add("is-visible"); }); }
  function setText(el, text) { if (el) el.textContent = text; }

  /* ---------- template ---------- */
  function serviceCard(s) {
    var m = { cutout: " card-media--cutout", contain: " card-media--contain" }[s.mode] || "";
    return '<article class="card reveal"><div class="card-media' + m + '"><div class="clip">' + img(s.img, s.name) +
      '</div><span class="card-icon">' + icon(s.icon) + '</span></div><div class="card-body"><h3>' + esc(s.name) +
      "</h3><p>" + esc(s.short) + '</p><a class="link-arrow" href="services.html#' + esc(s.id) + '">Selengkapnya ' + icon("arrow") + "</a></div></article>";
  }
  function sectorTile(s) {
    return '<div class="tile tile--dark reveal"><div class="tile-icon">' + icon(s.icon) + "</div><h3>" + esc(s.name) + "</h3><p>" + esc(s.desc) + "</p></div>";
  }
  function sectorCard(s) {
    var media = s.img
      ? '<div class="sector-ph" role="img" aria-label="' + esc(s.name) + '"><img src="' + esc(src(s.img)) + '" alt="" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:2"></div>'
      : '<div class="sector-ph" role="img" aria-label="Placeholder foto ' + esc(s.name) + '">' + icon(s.icon) + '<span class="ph-label">Foto menyusul</span></div>';
    return '<article class="sector-card reveal">' + media + '<div class="sector-body"><h3>' + esc(s.name) + "</h3><p>" + esc(s.desc) + "</p></div></article>";
  }
  function clientWall(c, withPlaceholders) {
    var h = c.clients.map(function (x) {
      return '<div class="logo-card reveal">' + (x.img ? '<img src="' + esc(src(x.img)) + '" alt="Logo ' + esc(x.name) + '" loading="lazy">' : "<span>" + esc(x.name) + "</span>") + "</div>";
    }).join("");
    if (withPlaceholders) {
      for (var i = 0; i < (c.client_placeholders || 0); i++) {
        h += '<div class="logo-card logo-card--ph reveal"><div>' + icon("image") + "<span>Logo klien<br>menyusul</span></div></div>";
      }
    }
    return h;
  }
  function serviceRow(s, n) {
    var m = { cutout: " is-cutout", contain: " is-contain" }[s.mode] || "";
    var paras = s.long.map(function (p) { return "<p>" + esc(p) + "</p>"; }).join("");
    var chips = s.chips.length ? '<div class="chips">' + s.chips.map(function (c) { return '<span class="chip">' + esc(c) + "</span>"; }).join("") + "</div>" : "";
    var subs = s.subs.length ? '<div class="sub-cards">' + s.subs.map(function (x) { return '<div class="sub-card"><h4>' + esc(x.title) + "</h4><p>" + esc(x.text) + "</p></div>"; }).join("") + "</div>" : "";
    var thumbs = s.extra_imgs.length ? '<div class="service-thumbs">' + s.extra_imgs.map(function (p) { return img(p, "Ilustrasi " + s.name); }).join("") + "</div>" : "";
    return '<article class="service-row reveal" id="' + esc(s.id) + '"><div class="service-media' + m + '">' + img(s.img, "Ilustrasi " + s.name) +
      '</div><div><div class="service-num">' + (n < 10 ? "0" : "") + n + '</div><div class="service-title"><span class="tile-icon">' + icon(s.icon) + "</span><h2>" + esc(s.name) + "</h2></div>" +
      paras + chips + subs + thumbs + '<p style="margin-top:1.2rem"><a class="btn btn--outline" href="contact.html">Tanya layanan ini</a></p></div></article>';
  }

  /* ---------- penerapan ke halaman ---------- */
  function apply(c) {
    var p = c.profile;

    // Profil (beranda & tentang kami)
    var ph = document.getElementById("profil-title");
    if (ph && ph.parentNode) {
      var ps = $$("p", ph.parentNode);
      setText(ps[0], p.about[0]); setText(ps[1], p.about[1]);
      if (document.getElementById("vmv-title")) { var strong = $("strong", ps[2] || ph.parentNode); setText(strong, p.belief); }
    }

    // Visi, Misi, Value, Tata Nilai, ERP (tentang kami)
    var cards = $$(".vmv-card");
    if (cards.length >= 4) {
      setText($("p", cards[1]), p.visi); setText($("p", cards[2]), p.misi); setText($("p", cards[3]), p.value);
      var vw = $(".value-words", cards[3]);
      if (vw) vw.innerHTML = p.value_words.map(function (w) { return "<span>" + esc(w) + "</span>"; }).join("");
    }
    var nilai = $('section[aria-labelledby="nilai-title"] p.reveal');
    setText(nilai, p.tata_nilai);
    var erp = document.getElementById("erp-title");
    if (erp && erp.parentNode) setText($("p", erp.parentNode), p.erp);

    // Layanan di beranda
    var svcGrid = $('section[aria-labelledby="layanan-title"] .grid--4');
    if (svcGrid) { svcGrid.innerHTML = c.services.map(serviceCard).join(""); reveal(svcGrid); }

    // Sektor: beranda (tile gelap) & halaman Fokus Bisnis (kartu)
    $$('section[aria-labelledby="sektor-title"] .grid--3').forEach(function (g) {
      g.innerHTML = c.sectors.map(g.classList.contains("sectors-dark") ? sectorTile : sectorCard).join("");
      reveal(g);
    });

    // Klien: beranda tanpa placeholder, halaman Klien dengan placeholder
    var onClientsPage = !!document.getElementById("portfolio-title");
    $$('section[aria-labelledby="klien-title"] .logo-wall').forEach(function (w) {
      w.innerHTML = clientWall(c, onClientsPage); reveal(w);
    });

    // Halaman Layanan: indeks + baris layanan
    var list = $('section[aria-label="Daftar layanan"] .container');
    if (list) {
      var idx = $(".service-index", list);
      if (idx) idx.innerHTML = c.services.map(function (s) { return '<a href="#' + esc(s.id) + '">' + esc(s.name.replace("Jagaraya ", "")) + "</a>"; }).join("");
      $$(".service-row", list).forEach(function (r) { r.parentNode.removeChild(r); });
      list.insertAdjacentHTML("beforeend", c.services.map(function (s, i) { return serviceRow(s, i + 1); }).join(""));
      reveal(list);
      if (location.hash) { var t = document.getElementById(location.hash.slice(1)); if (t) t.scrollIntoView(); }
    }

    // Formulir kontak: pilihan layanan
    var sel = document.getElementById("f-service");
    if (sel) {
      var keep = sel.value;
      sel.innerHTML = '<option value="">Pilih layanan</option>' +
        c.services.map(function (s) { return '<option value="' + esc(s.name) + '">' + esc(s.name) + "</option>"; }).join("") +
        '<option value="Lainnya">Lainnya / belum yakin</option>';
      sel.value = keep;
    }
  }

  fetch("/api/content", { headers: { Accept: "application/json" } })
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (d) { if (d && d.published && d.content) apply(d.content); })
    .catch(function () { /* HTML bawaan tetap tampil */ });
})();
