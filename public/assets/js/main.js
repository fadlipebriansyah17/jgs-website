(function () {
  "use strict";
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- Header: menu mobile + bayangan saat scroll ---------- */
  var header = $(".site-header");
  var toggle = $(".nav-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    $$(".nav a").forEach(function (a) {
      a.addEventListener("click", function () {
        document.body.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { document.body.classList.remove("nav-open"); toggle.setAttribute("aria-expanded", "false"); }
    });
  }
  function onScroll() { if (header) header.classList.toggle("is-scrolled", window.scrollY > 8); }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---------- Animasi muncul saat scroll ---------- */
  var items = $$(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-visible"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    items.forEach(function (el, i) {
      el.style.transitionDelay = (i % 4) * 70 + "ms";
      io.observe(el);
    });
  } else {
    items.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* ---------- Formulir kontak ---------- */
  var form = $("#contact-form");
  if (!form) return;
  var t = window.JGS.t;
  var notice = $("#form-notice");
  var waBtn = $("#form-wa");

  function setError(field, msg) {
    var wrap = field.closest(".field");
    if (!wrap) return;
    wrap.classList.toggle("has-error", !!msg);
    var err = $(".field-error", wrap);
    if (err) err.textContent = msg || "";
    field.setAttribute("aria-invalid", msg ? "true" : "false");
  }

  function validateField(f) {
    var v = (f.type === "checkbox" ? f.checked : f.value.trim());
    var msg = "";
    if (f.required && (f.type === "checkbox" ? !v : !v)) msg = f.type === "checkbox" ? t("consent") : t("required");
    else if (v && f.name === "email" && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)) msg = t("invalidEmail");
    else if (v && f.name === "phone") {
      var digits = v.replace(/\D/g, "");
      if (!/^[0-9+()\-\s]+$/.test(v) || digits.length < 8 || digits.length > 15) msg = t("invalidPhone");
    } else if (v && f.name === "message" && v.length < 10) msg = t("minMessage");
    setError(f, msg);
    return !msg;
  }

  var fields = $$("input, select, textarea", form).filter(function (f) { return f.name && f.name !== "website"; });
  fields.forEach(function (f) {
    f.addEventListener("blur", function () { validateField(f); });
    f.addEventListener("input", function () { if (f.closest(".field").classList.contains("has-error")) validateField(f); });
  });

  function buildWaText() {
    var g = function (n) { var el = form.elements[n]; return el ? (el.value || "").trim() : ""; };
    var lines = [t("waIntro")];
    if (g("name")) lines.push("Nama: " + g("name"));
    if (g("company")) lines.push("Perusahaan: " + g("company"));
    if (g("service")) lines.push("Layanan: " + g("service"));
    if (g("phone")) lines.push("Telepon: " + g("phone"));
    if (g("message")) lines.push("Pesan: " + g("message"));
    return lines.join("\n");
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var ok = true, first = null;
    fields.forEach(function (f) { if (!validateField(f)) { ok = false; if (!first) first = f; } });
    if (form.elements.website && form.elements.website.value) return; // honeypot (bot)
    if (!ok) { if (first) first.focus(); return; }

    var cfg = window.JGS.config;
    if (cfg.contactEndpoint) {
      var data = {};
      fields.forEach(function (f) { data[f.name] = f.type === "checkbox" ? f.checked : f.value.trim(); });
      fetch(cfg.contactEndpoint, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data) })
        .then(function (r) { if (!r.ok) throw new Error(r.status); notice.className = "notice notice--ok"; notice.textContent = "Terima kasih, pesan Anda telah terkirim."; notice.hidden = false; form.reset(); })
        .catch(function () { notice.className = "notice"; notice.textContent = t("pending"); notice.hidden = false; });
      return;
    }
    notice.className = "notice";
    notice.textContent = t("pending");
    notice.hidden = false;
    if (waBtn) { waBtn.href = window.JGS.waLink(buildWaText()); waBtn.hidden = false; }
    notice.scrollIntoView({ behavior: "smooth", block: "nearest" });
  });
})();
