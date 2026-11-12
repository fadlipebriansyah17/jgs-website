# -*- coding: utf-8 -*-
"""
Generator halaman statis JGS.

Jalankan dari folder proyek:   python3 tools/build.py
Hasil: public/*.html + public/admin/index.html (HTML biasa, tanpa dependensi runtime).

Konten diambil dari tools/content_id.py. Untuk bahasa lain, tambahkan content_<kode>.py
dan daftarkan di LANGS.
"""
import html
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
PUBLIC = os.path.join(os.path.dirname(HERE), "public")

LANGS = ["id"]          # tambahkan "en" setelah content_en.py dibuat
DEFAULT_LANG = "id"
C = importlib.import_module("content_%s" % DEFAULT_LANG)
S = C.SITE

e = html.escape

ICONS = {
    "shield": "M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z|M9 12l2 2 4-4",
    "sparkle": "M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z|M19 3v4|M17 5h4",
    "users": "M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2|M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z|M22 21v-2a4 4 0 0 0-3-3.9|M16 3.1a4 4 0 0 1 0 7.8",
    "parking": "M4 4h16v16H4z|M9 17V7h4a3 3 0 0 1 0 6H9",
    "bug": "M8 8h8v7a4 4 0 0 1-8 0z|M9 5l1.5 2|M15 5l-1.5 2|M3 10h5|M16 10h5|M3 18l5-2|M21 18l-5-2|M12 8v11",
    "camera": "M3 7h4l2-3h6l2 3h4v13H3z|M12 17a4 4 0 1 0 0-8 4 4 0 0 0 0 8z",
    "truck": "M2 6h11v10H2z|M13 9h4l4 4v3h-8z|M7 19a2 2 0 1 0 0-4 2 2 0 0 0 0 4z|M17 19a2 2 0 1 0 0-4 2 2 0 0 0 0 4z",
    "leaf": "M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z|M2 21c0-3 1.9-5.5 6-7",
    "building": "M4 21V4h10v17|M14 9h6v12|M8 8h2|M8 12h2|M8 16h2|M2 21h20",
    "bank": "M3 10l9-6 9 6|M5 10v8|M9 10v8|M15 10v8|M19 10v8|M3 21h18",
    "factory": "M2 21V10l6 4v-4l6 4v-4l6 4v7z|M17 3v7|M2 21h20",
    "box": "M21 8l-9-5-9 5v8l9 5 9-5z|M3 8l9 5 9-5|M12 13v8",
    "hospital": "M4 21V5h16v16|M12 9v6|M9 12h6|M2 21h20",
    "home": "M3 11l9-8 9 8|M5 10v11h14V10|M10 21v-6h4v6",
    "bed": "M3 18V6|M3 14h18v4|M21 14v-2a3 3 0 0 0-3-3h-7v5|M7.5 11.5h.01",
    "bag": "M5 8h14l-1 13H6z|M9 8V6a3 3 0 0 1 6 0v2",
    "cap": "M2 9l10-5 10 5-10 5z|M6 11.5V16c0 1.5 3 3 6 3s6-1.5 6-3v-4.5|M22 9v6",
    "check": "M5 12l5 5 9-10",
    "phone": "M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z",
    "pin": "M12 22s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z|M12 12a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z",
    "chat": "M21 12a8 8 0 0 1-11.7 7L3 21l2-5.5A8 8 0 1 1 21 12z",
    "arrow": "M5 12h14|M13 6l6 6-6 6",
    "target": "M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20z|M12 18a6 6 0 1 0 0-12 6 6 0 0 0 0 12z|M12 14a2 2 0 1 0 0-4 2 2 0 0 0 0 4z",
    "eye": "M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z|M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z",
    "flag": "M5 21V4|M5 4h13l-2 4 2 4H5",
    "heart": "M12 20s-8-5-8-11a4.5 4.5 0 0 1 8-2.5A4.5 4.5 0 0 1 20 9c0 6-8 11-8 11z",
    "layers": "M12 3l9 5-9 5-9-5z|M3 13l9 5 9-5",
    "chart": "M4 20V4|M4 20h16|M8 16v-4|M12 16V8|M16 16v-6",
    "doc": "M6 3h9l4 4v14H6z|M14 3v5h5|M9 13h6|M9 17h6",
    "cog": "M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z|M12 2v3|M12 19v3|M2 12h3|M19 12h3|M5 5l2 2|M17 17l2 2|M19 5l-2 2|M7 17l-2 2",
    "server": "M3 4h18v6H3z|M3 14h18v6H3z|M7 7h.01|M7 17h.01",
    "image": "M3 4h18v16H3z|M3 16l5-5 4 4 3-3 6 6|M9 9h.01",
    "plus": "M12 5v14|M5 12h14",
}


def icon(name, cls="icon"):
    paths = "".join('<path d="%s"/>' % d for d in ICONS[name].split("|"))
    return '<svg class="%s" viewBox="0 0 24 24" aria-hidden="true">%s</svg>' % (cls, paths)


def img(path, alt, root, cls="", loading="lazy", w=None, h=None):
    size = (' width="%d" height="%d"' % (w, h)) if w and h else ""
    c = (' class="%s"' % cls) if cls else ""
    return '<img%s src="%sassets/images/%s" alt="%s" loading="%s"%s>' % (c, root, path, e(alt), loading, size)


# ---------------------------------------------------------------- layout
def head(title, desc, root, page_file):
    full_title = "%s | %s (JGS)" % (title, "Jagaraya Global Services") if page_file != "index.html" else "Jagaraya Global Services (JGS) | Facility Service Solution"
    canon = S["url"] + "/" + ("" if page_file == "index.html" else page_file)
    return """<!DOCTYPE html>
<html lang="%(lang)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(canon)s">
<meta name="theme-color" content="#102747">
<meta property="og:type" content="website">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(canon)s">
<meta property="og:image" content="%(url)s/assets/images/logo/jgs-shield.png">
<link rel="icon" type="image/png" href="%(root)sassets/images/logo/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Playfair+Display:wght@600;700&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="%(root)sassets/css/tokens.css">
<link rel="stylesheet" href="%(root)sassets/css/base.css">
<link rel="stylesheet" href="%(root)sassets/css/components.css">
<link rel="stylesheet" href="%(root)sassets/css/pages.css">
</head>
""" % dict(lang=DEFAULT_LANG, title=e(full_title), desc=e(desc), canon=canon, url=S["url"], root=root)


def header(root, current):
    links = "".join(
        '<a href="%s%s"%s>%s</a>' % (root, f, ' aria-current="page"' if k == current else "", e(label))
        for f, label, k in C.NAV
    )
    return """<body>
<a class="skip-link" href="#main">Lewati ke konten</a>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="%(root)sindex.html" aria-label="JGS - Beranda">
      %(logo)s
      <span class="brand-text"><strong>JAGARAYA</strong><span>GLOBAL SERVICES</span></span>
    </a>
    <button class="nav-toggle" type="button" aria-label="Buka menu" aria-expanded="false" aria-controls="nav"><span></span></button>
    <nav class="nav" id="nav" aria-label="Navigasi utama">%(links)s</nav>
  </div>
</header>
<main id="main">
""" % dict(root=root, links=links, logo=img("logo/jgs-shield.png", "Logo Jagaraya Global Services", root, loading="eager", w=50, h=59))


def cta_band(root):
    return """<section class="cta-band" aria-labelledby="cta-title">
  <div class="container cta-inner">
    <div>
      <h2 id="cta-title">Siap berdiskusi tentang kebutuhan layanan Anda?</h2>
      <p>Hubungi tim JGS untuk membahas solusi facility service yang sesuai dengan properti dan bisnis Anda.</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-wa btn--wa" href="https://wa.me/%(wa)s" target="_blank" rel="noopener">%(chat)s Chat WhatsApp</a>
      <a class="btn btn--ghost" href="%(root)scontact.html">Hubungi Kami</a>
    </div>
  </div>
</section>
""" % dict(wa=S["wa"], chat=icon("chat"), root=root)


def footer(root):
    nav = "".join('<li><a href="%s%s">%s</a></li>' % (root, f, e(l)) for f, l, k in C.NAV)
    svc = "".join('<li><a href="%sservices.html#%s">%s</a></li>' % (root, s["id"], e(s["name"])) for s in C.SERVICES[:4])
    addr = "<br>".join(e(x) for x in S["address_lines"])
    return """</main>
<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      %(logo)s
      <p><strong style="color:#fff">%(name)s</strong><br>%(tag)s</p>
      <p>Penyedia sumber daya manusia dan layanan alihdaya untuk berbagai sektor industri bisnis. Bagian dari Jagaraya Group.</p>
    </div>
    <div>
      <h4>Navigasi</h4>
      <ul>%(nav)s</ul>
    </div>
    <div>
      <h4>Kontak</h4>
      <ul class="footer-contact">
        <li>%(pin)s<span>%(addr)s</span></li>
        <li>%(phone)s<a href="tel:%(tel)s">%(phoned)s</a></li>
        <li>%(chat)s<a href="https://wa.me/%(wa)s" target="_blank" rel="noopener">WhatsApp</a></li>
        <li>%(arrow)s<a href="https://%(domain)s">%(domain)s</a></li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>&copy; <span id="year">2025</span> %(name)s. Hak cipta dilindungi.</span>
    <span>Foto pada website ini bersifat ilustrasi dan akan diganti dengan dokumentasi resmi perusahaan.</span>
  </div>
</footer>
<a class="wa-float" href="https://wa.me/%(wa)s" target="_blank" rel="noopener" aria-label="Chat WhatsApp JGS">%(chat)s</a>
<script src="%(root)sassets/js/components.js"></script>
<script src="%(root)sassets/js/main.js"></script>
<script>document.getElementById("year").textContent = new Date().getFullYear();</script>
</body>
</html>
""" % dict(
        logo=img("logo/jagaraya-group.png", "Logo Jagaraya Group", root, w=64, h=64), name=S["name"], tag=S["tagline"],
        nav=nav, svc=svc, pin=icon("pin"), addr=addr, phone=icon("phone"), tel=S["phone_tel"], phoned=S["phone_display"],
        chat=icon("chat"), wa=S["wa"], arrow=icon("arrow"), domain=S["domain"], root=root,
    )


def page_hero(title, lead, crumb, root):
    return """<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="%sindex.html">Beranda</a> / %s</div>
    <h1>%s</h1>
    <p>%s</p>
  </div>
</section>
""" % (root, e(crumb), e(title), e(lead))


def section_head(eyebrow, title, lead="", center=False):
    cls = "section-head section-head--center reveal" if center else "section-head reveal"
    lead_html = "<p>%s</p>" % e(lead) if lead else ""
    return '<div class="%s"><span class="eyebrow">%s</span><h2>%s</h2>%s</div>' % (cls, e(eyebrow), e(title), lead_html)


# ---------------------------------------------------------------- blocks
def service_card(s, root):
    mode = s["mode"]
    mcls = {"cutout": " card-media--cutout", "contain": " card-media--contain"}.get(mode, "")
    return """<article class="card reveal">
  <div class="card-media%s"><div class="clip">%s</div><span class="card-icon">%s</span></div>
  <div class="card-body">
    <h3>%s</h3>
    <p>%s</p>
    <a class="link-arrow" href="%sservices.html#%s">Selengkapnya %s</a>
  </div>
</article>""" % (mcls, img(s["img"], s["name"], root), icon(s["icon"]), e(s["name"]), e(s["short"]), root, s["id"], icon("arrow"))


def sector_tile(name, desc, ic):
    return '<div class="tile tile--dark reveal"><div class="tile-icon">%s</div><h3>%s</h3><p>%s</p></div>' % (icon(ic), e(name), e(desc))


def sector_card(name, desc, ic):
    return """<article class="sector-card reveal">
  <div class="sector-ph" role="img" aria-label="Placeholder foto %s">%s<span class="ph-label">Foto menyusul</span></div>
  <div class="sector-body"><h3>%s</h3><p>%s</p></div>
</article>""" % (e(name), icon(ic), e(name), e(desc))


def add_value_block():
    jgs = "".join("<li>%s<span>%s</span></li>" % (icon(i), e(n)) for n, i in C.ADD_VALUE_JGS)
    ops = "".join("<li>%s<span>%s</span></li>" % (icon(i), e(n)) for n, i in C.ADD_VALUE_OPS)
    kb = "".join("<li>%s<span>%s</span></li>" % (icon("check"), e(x)) for x in C.KEY_BENEFIT)
    return """<div class="addval reveal">
  <div class="addval-col"><h3>Dari sisi Klien &amp; Kontrak</h3><ul>%s</ul></div>
  <div class="addval-col addval-col--dark"><h3>Dikelola oleh JGS</h3><ul class="addval-cols2">%s</ul></div>
</div>
<div class="keybenefit reveal"><h3>Key Benefit</h3><ul class="check-list">%s</ul></div>""" % (jgs, ops, kb)


def client_wall(root, placeholders=True):
    cards = "".join('<div class="logo-card reveal">%s</div>' % img(c["img"], "Logo " + c["name"], root) for c in C.CLIENTS)
    if placeholders:
        cards += "".join(
            '<div class="logo-card logo-card--ph reveal"><div>%s<span>Logo klien<br>menyusul</span></div></div>' % icon("image")
            for _ in range(C.CLIENT_PLACEHOLDERS)
        )
    return '<div class="logo-wall">%s</div>' % cards


# ---------------------------------------------------------------- pages
def page_home():
    root = ""
    services = "".join(service_card(s, root) for s in C.SERVICES)
    sectors = "".join(sector_tile(*x) for x in C.SECTORS)
    why = [
        ("Manajemen solid &amp; kokoh", "Didukung manajemen yang kuat untuk bersaing di industri facility service dan jasa keamanan di Indonesia.", "flag"),
        ("SDM terdidik, terlatih &amp; profesional", "Investasi pada perekrutan, pelatihan, dan pengembangan keterampilan setiap karyawan.", "users"),
        ("Kekuatan finansial", "Mendukung keberlangsungan layanan bagi seluruh pengguna jasa.", "chart"),
        ("Metode kerja tertata", "Pendekatan Man – Money – Method &amp; Materials yang terstruktur.", "doc"),
        ("Sistem ERP", "Pengelolaan operasional yang sistematis, efisien, dan efektif.", "server"),
        ("SLA &amp; KPI terukur", "Pengendalian pelaksanaan layanan dapat dilakukan melalui SLA/KPI.", "target"),
    ]
    why_html = "".join('<div class="tile reveal"><div class="tile-icon">%s</div><h3>%s</h3><p>%s</p></div>' % (icon(i), t, d) for t, d, i in why)
    body = """
<section class="hero" aria-labelledby="hero-title">
  <div class="container hero-inner">
    <div>
      <span class="hero-tag">%(tag)s</span>
      <h1 id="hero-title">Mitra andal untuk <em>facility service</em> dan alihdaya Anda</h1>
      <p class="lead">Jagaraya Global Services menyediakan sumber daya manusia berkualitas tinggi dengan keahlian, kompetensi, dan integritas untuk berbagai sektor industri bisnis.</p>
      <div class="hero-actions">
        <a class="btn btn--primary" href="services.html">Lihat Layanan %(arrow)s</a>
        <a class="btn btn--ghost" href="contact.html">Hubungi Kami</a>
      </div>
    </div>
    <div class="hero-visual" aria-hidden="true">
      %(shield)s
      %(p1)s
      %(p2)s
    </div>
  </div>
</section>

<section class="section" aria-labelledby="profil-title">
  <div class="container split">
    <div class="split-media reveal">
      %(grp)s
      %(guard)s
    </div>
    <div class="reveal">
      <span class="eyebrow">Profil Singkat</span>
      <h2 id="profil-title">Investasi pada manusia adalah kunci pelayanan kelas utama</h2>
      <p>%(about1)s</p>
      <p>%(about2)s</p>
      <a class="btn btn--outline" href="about.html">Tentang JGS</a>
    </div>
  </div>
</section>

<section class="section section--surface" aria-labelledby="layanan-title">
  <div class="container">
    %(sh_services)s
    <div class="grid grid--4">%(services)s</div>
    <p style="text-align:center;margin-top:2.5rem"><a class="btn btn--primary" href="services.html">Semua Layanan %(arrow)s</a></p>
  </div>
</section>

<section class="section section--navy" aria-labelledby="sektor-title">
  <div class="container">
    %(sh_sectors)s
    <div class="grid grid--3 sectors-dark">%(sectors)s</div>
    <p style="text-align:center;margin-top:2.5rem"><a class="btn btn--ghost" href="business-focus.html">Lihat Fokus Bisnis</a></p>
  </div>
</section>

<section class="section" aria-labelledby="keunggulan-title">
  <div class="container">
    %(sh_why)s
    <div class="grid grid--3 why-grid">%(why)s</div>
  </div>
</section>

<section class="section section--surface" aria-labelledby="addval-title">
  <div class="container">
    %(sh_add)s
    %(add)s
  </div>
</section>

<section class="section" aria-labelledby="klien-title">
  <div class="container">
    %(sh_clients)s
    %(clients)s
    <p style="text-align:center;margin-top:2rem"><a class="link-arrow" href="clients.html">Halaman Klien %(arrow)s</a></p>
  </div>
</section>

%(cta)s

<section class="section" aria-labelledby="kontak-title">
  <div class="container">
    %(sh_contact)s
    <div class="grid grid--3">
      <div class="tile reveal"><div class="tile-icon">%(pin)s</div><h3>Kantor Pusat</h3><p>%(addr)s</p></div>
      <div class="tile reveal"><div class="tile-icon">%(phone)s</div><h3>Telepon</h3><p><a href="tel:%(tel)s">%(phoned)s</a></p></div>
      <div class="tile reveal"><div class="tile-icon">%(chat)s</div><h3>WhatsApp</h3><p><a href="https://wa.me/%(wa)s" target="_blank" rel="noopener">Chat langsung dengan tim kami</a></p></div>
    </div>
  </div>
</section>
""" % dict(
        tag=S["tagline"], arrow=icon("arrow"),
        shield=img("logo/jgs-shield.png", "", root, cls="shield", loading="eager"),
        p1=img("general/guard-2.png", "", root, cls="person", loading="eager"),
        p2=img("general/guard-1.png", "", root, cls="person person--2", loading="eager"),
        grp=img("logo/jagaraya-group.png", "Jagaraya Group", root, cls="logo-bg"),
        guard=img("general/guard-1.png", "Ilustrasi petugas keamanan", root),
        about1=e(C.ABOUT[0]), about2=e(C.ABOUT[1]),
        sh_services=section_head("Layanan Utama", "Delapan layanan terintegrasi untuk kebutuhan properti dan bisnis Anda", "Dari keamanan hingga pengelolaan limbah, JGS menghadirkan solusi facility service dalam satu mitra.").replace("<h2>", '<h2 id="layanan-title">'),
        services=services,
        sh_sectors=section_head("Fokus Bisnis", "Sektor yang kami layani", "Pengalaman melayani beragam sektor industri bisnis.").replace("<h2>", '<h2 id="sektor-title">'),
        sectors=sectors,
        sh_why=section_head("Keunggulan JGS", "Mengapa memilih Jagaraya Global Services", center=True).replace("<h2>", '<h2 id="keunggulan-title">'),
        why=why_html,
        sh_add=section_head("Additional Value", "Nilai tambah dalam setiap kerja sama", "Pengelolaan layanan yang terukur melalui proses bisnis, SLA, dan KPI.").replace("<h2>", '<h2 id="addval-title">'),
        add=add_value_block(),
        sh_clients=section_head("Area Klien", "Dipercaya oleh berbagai bidang usaha", "Berikut sebagian logo klien yang tercantum pada Company Profile JGS 2025.", center=True).replace("<h2>", '<h2 id="klien-title">'),
        clients=client_wall(root, placeholders=False),
        cta=cta_band(root),
        sh_contact=section_head("Informasi Kontak", "Kunjungi atau hubungi kami", center=True).replace("<h2>", '<h2 id="kontak-title">'),
        pin=icon("pin"), addr="<br>".join(e(x) for x in S["address_lines"][1:]), phone=icon("phone"), tel=S["phone_tel"], phoned=S["phone_display"],
        chat=icon("chat"), wa=S["wa"],
    )
    return "index.html", head("Beranda", "Jagaraya Global Services (JGS) - Facility Service Solution. Layanan security, house keeping, HR provider, parking, pest control, security system & safety, transportation & logistic, dan waste management.", root, "index.html") + header(root, "home") + body + footer(root)


def page_about():
    root = ""
    vmv = """<div class="vmv">
  <div class="vmv-card reveal"><div class="vmv-icon">%s</div><h3>Karakter</h3><p>Kami berkarakter profesional, berdedikasi, berkinerja tinggi, dan berintegritas dalam setiap layanan.</p></div>
  <div class="vmv-card reveal"><div class="vmv-icon">%s</div><h3>Visi</h3><p>%s</p></div>
  <div class="vmv-card reveal"><div class="vmv-icon">%s</div><h3>Misi</h3><p>%s</p></div>
  <div class="vmv-card reveal" style="grid-column:1/-1"><div class="vmv-icon">%s</div><h3>Value</h3><p>%s</p><div class="value-words">%s</div></div>
</div>""" % (
        icon("heart"), icon("eye"), e(C.VISI), icon("flag"), e(C.MISI), icon("target"), e(C.VALUE),
        "".join("<span>%s</span>" % e(w) for w in C.VALUE_WORDS),
    )
    four = "".join('<div class="tile reveal"><div class="tile-icon">%s</div><h3>%s</h3><p>%s</p></div>' % (icon(i), e(n), e(d)) for n, d, i in C.FOUR_M)
    body = page_hero("Tentang Kami", "Perusahaan penyedia sumber daya manusia berkualitas dan layanan alihdaya untuk berbagai sektor industri bisnis.", "Tentang Kami", root) + """
<section class="section" aria-labelledby="profil-title">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Profil Perusahaan</span>
      <h2 id="profil-title">Jagaraya Global Services</h2>
      <p>%(a1)s</p>
      <p>%(a2)s</p>
      <p><strong>%(belief)s</strong></p>
    </div>
    <div class="split-media reveal">%(grp)s%(g)s</div>
  </div>
</section>

<section class="section section--surface" aria-labelledby="vmv-title">
  <div class="container">
    %(sh_vmv)s
    %(vmv)s
  </div>
</section>

<section class="section" aria-labelledby="nilai-title">
  <div class="container">
    %(sh_nilai)s
    <p class="reveal" style="max-width:860px;font-size:1.08rem">%(tata)s</p>
    <div class="grid grid--4 four-m" style="margin-top:2rem">%(four)s</div>
  </div>
</section>

<section class="section section--surface" aria-labelledby="erp-title">
  <div class="container">
    <div class="erp-box reveal">
      <div class="erp-icon">%(server)s</div>
      <div><h3 id="erp-title">Sistem ERP (Enterprise Resources Planning)</h3><p>%(erp)s</p></div>
    </div>
  </div>
</section>

%(cta)s
""" % dict(
        a1=e(C.ABOUT[0]), a2=e(C.ABOUT[1]), belief=e(C.ABOUT_BELIEF),
        grp=img("logo/jagaraya-group.png", "Jagaraya Group", root, cls="logo-bg"), g=img("general/guard-back.png", "Ilustrasi petugas keamanan", root),
        sh_vmv=section_head("Visi, Misi, Karakter &amp; Value".replace("&amp;", "&"), "Arah dan nilai yang kami pegang", center=True).replace("<h2>", '<h2 id="vmv-title">'),
        vmv=vmv,
        sh_nilai=section_head("Tata Nilai Perusahaan", "Man – Money – Method & Materials").replace("<h2>", '<h2 id="nilai-title">'),
        tata=e(C.TATA_NILAI), four=four, server=icon("server"), erp=e(C.ERP), cta=cta_band(root),
    )
    return "about.html", head("Tentang Kami", "Profil, visi, misi, karakter, value, tata nilai perusahaan, pendekatan Man-Money-Method-Materials, dan sistem ERP Jagaraya Global Services.", root, "about.html") + header(root, "about") + body + footer(root)


def page_services():
    root = ""
    idx = "".join('<a href="#%s">%s</a>' % (s["id"], e(s["name"].replace("Jagaraya ", ""))) for s in C.SERVICES)
    rows = []
    for n, s in enumerate(C.SERVICES, 1):
        mode_cls = {"cutout": " is-cutout", "contain": " is-contain"}.get(s["mode"], "")
        paras = "".join("<p>%s</p>" % e(p) for p in s["long"])
        chips = ('<div class="chips">%s</div>' % "".join('<span class="chip">%s</span>' % e(c) for c in s["chips"])) if s.get("chips") else ""
        subs = ('<div class="sub-cards">%s</div>' % "".join('<div class="sub-card"><h4>%s</h4><p>%s</p></div>' % (e(a), e(b)) for a, b in s["subs"])) if s.get("subs") else ""
        thumbs = ('<div class="service-thumbs">%s</div>' % "".join(img(p, "Ilustrasi " + s["name"], root) for p in s["extra_imgs"])) if s.get("extra_imgs") else ""
        rows.append("""<article class="service-row reveal" id="%(id)s">
  <div class="service-media%(m)s">%(img)s</div>
  <div>
    <div class="service-num">0%(n)d</div>
    <div class="service-title"><span class="tile-icon">%(ic)s</span><h2>%(name)s</h2></div>
    %(paras)s%(chips)s%(subs)s%(thumbs)s
    <p style="margin-top:1.2rem"><a class="btn btn--outline" href="contact.html">Tanya layanan ini</a></p>
  </div>
</article>""" % dict(id=s["id"], m=mode_cls, img=img(s["img"], "Ilustrasi " + s["name"], root), n=n, ic=icon(s["icon"]), name=e(s["name"]), paras=paras, chips=chips, subs=subs, thumbs=thumbs))
    body = page_hero("Layanan Kami", "Delapan layanan facility service yang dikelola secara terstruktur oleh Jagaraya Global Services.", "Layanan", root) + """
<section class="section" aria-label="Daftar layanan">
  <div class="container">
    <div class="service-index reveal">%s</div>
    %s
  </div>
</section>
%s
""" % (idx, "".join(rows), cta_band(root))
    return "services.html", head("Layanan", "Delapan layanan JGS: Security Service, House Keeping, HR Provider, Parking Management, Pest Control, Security System & Safety, Transportation & Logistic, dan Waste Management.", root, "services.html") + header(root, "services") + body + footer(root)


def page_business():
    root = ""
    cards = "".join(sector_card(*x) for x in C.SECTORS)
    body = page_hero("Fokus Bisnis", "Sektor industri dan properti yang kami layani dengan sumber daya manusia profesional.", "Fokus Bisnis", root) + """
<section class="section" aria-labelledby="sektor-title">
  <div class="container">
    %s
    <div class="grid grid--3">%s</div>
    <p class="reveal" style="margin-top:1.5rem;color:var(--muted);font-size:.88rem">Area foto saat ini berupa placeholder dan mudah diganti dengan dokumentasi resmi (folder <code>assets/images/business-focus/</code>).</p>
  </div>
</section>

<section class="section section--surface" aria-labelledby="addval-title">
  <div class="container">
    %s
    %s
  </div>
</section>
%s
""" % (
        section_head("Sembilan Sektor", "Bisnis fokus kami", "Setiap sektor memiliki kebutuhan operasional yang berbeda. JGS menyesuaikan SOP dan tenaga kerja dengan lokasi tempat kami bekerja.").replace("<h2>", '<h2 id="sektor-title">'),
        cards,
        section_head("Additional Value", "Nilai tambah JGS untuk klien", "Berlaku di seluruh sektor yang kami layani.").replace("<h2>", '<h2 id="addval-title">'),
        add_value_block(), cta_band(root),
    )
    return "business-focus.html", head("Fokus Bisnis", "Sektor yang dilayani JGS: office building, banks, industrial plant, logistic & retail, hospital, apartment, hotel, mall, dan school & campus.", root, "business-focus.html") + header(root, "business") + body + footer(root)


def page_clients():
    root = ""
    body = page_hero("Klien Kami", "Portofolio klien Jagaraya Global Services.", "Klien", root) + """
<section class="section" aria-labelledby="klien-title">
  <div class="container">
    %s
    %s
    <div class="notice reveal" style="margin-top:2rem">Logo di atas bersumber dari Company Profile JGS 2025 dan perlu dikonfirmasi izin tampilnya sebelum website dipublikasikan. Slot kosong adalah placeholder untuk klien lain; daftar klien akan dilengkapi setelah nama dan logo dikonfirmasi.</div>
  </div>
</section>

<section class="section section--surface" aria-labelledby="portfolio-title">
  <div class="container">
    %s
    <div class="grid grid--3">%s</div>
  </div>
</section>
%s
""" % (
        section_head("Area Klien", "Dipercaya oleh berbagai bidang usaha", center=True).replace("<h2>", '<h2 id="klien-title">'),
        client_wall(root),
        section_head("Portofolio", "Studi kasus dan proyek", "Bagian ini disiapkan untuk menampilkan portofolio proyek setelah data dan izin tampil dari klien tersedia.", center=True).replace("<h2>", '<h2 id="portfolio-title">'),
        "".join(
            '<div class="tile reveal"><div class="tile-icon">%s</div><h3>Portofolio %d</h3><p>Placeholder: nama klien, layanan yang diberikan, dan periode kerja sama akan diisi setelah dikonfirmasi.</p></div>' % (icon("plus"), i)
            for i in (1, 2, 3)
        ),
        cta_band(root),
    )
    return "clients.html", head("Klien", "Portofolio dan area klien Jagaraya Global Services (JGS).", root, "clients.html") + header(root, "clients") + body + footer(root)


def page_contact():
    root = ""
    opts = "".join('<option value="%s">%s</option>' % (e(s["name"]), e(s["name"])) for s in C.SERVICES) + '<option value="Lainnya">Lainnya / belum yakin</option>'
    maps = "https://www.google.com/maps?q=%s&output=embed" % S["map_query"].replace(" ", "+")
    maps_link = "https://www.google.com/maps/search/?api=1&query=%s" % S["map_query"].replace(" ", "+")
    body = page_hero("Hubungi Kami", "Sampaikan kebutuhan Anda. Tim JGS siap berdiskusi mengenai solusi yang sesuai.", "Kontak", root) + """
<section class="section" aria-labelledby="kontak-title">
  <div class="container contact-grid">
    <div class="contact-card reveal">
      <h3 id="kontak-title">Informasi Kontak</h3>
      <ul class="contact-list">
        <li><span class="ci">%(pin)s</span><div><strong>Kantor Pusat</strong>%(addr)s</div></li>
        <li><span class="ci">%(phone)s</span><div><strong>Telepon</strong><a href="tel:%(tel)s">%(phoned)s</a></div></li>
        <li><span class="ci">%(arrow)s</span><div><strong>Website</strong><a href="https://%(domain)s">%(domain)s</a></div></li>
      </ul>
      <p style="margin-top:1.2rem"><a class="btn btn--wa" href="https://wa.me/%(wa)s" target="_blank" rel="noopener">%(chat)s Chat via WhatsApp</a></p>
    </div>

    <div class="form-card reveal">
      <h3>Kirim Pesan</h3>
      <div class="notice" style="margin-bottom:1.2rem">Pengiriman formulir akan diaktifkan setelah backend tersedia. Sementara itu, setelah formulir divalidasi Anda dapat melanjutkan lewat WhatsApp.</div>
      <form id="contact-form" class="form" novalidate>
        <div class="form-row">
          <div class="field"><label for="f-name">Nama lengkap <span class="req">*</span></label><input id="f-name" name="name" type="text" autocomplete="name" required><div class="field-error" role="alert"></div></div>
          <div class="field"><label for="f-company">Perusahaan / instansi</label><input id="f-company" name="company" type="text" autocomplete="organization"><div class="field-error" role="alert"></div></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="f-phone">Telepon / WhatsApp <span class="req">*</span></label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required><div class="field-error" role="alert"></div></div>
          <div class="field"><label for="f-email">Email <span class="req">*</span></label><input id="f-email" name="email" type="email" autocomplete="email" required><div class="field-error" role="alert"></div></div>
        </div>
        <div class="field"><label for="f-service">Layanan yang diminati</label><select id="f-service" name="service"><option value="">Pilih layanan</option>%(opts)s</select><div class="field-error" role="alert"></div></div>
        <div class="field"><label for="f-message">Pesan <span class="req">*</span></label><textarea id="f-message" name="message" required></textarea><div class="field-error" role="alert"></div></div>
        <div class="hp" aria-hidden="true"><label>Website <input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
        <div class="field field--check"><input id="f-consent" name="consent" type="checkbox" required><label for="f-consent">Saya menyetujui data saya digunakan oleh JGS untuk menanggapi permintaan ini. <span class="req">*</span></label><div class="field-error" role="alert"></div></div>
        <div><button class="btn btn--primary" type="submit">Kirim Pesan %(arrowi)s</button></div>
        <div id="form-notice" class="notice" role="status" hidden></div>
        <a id="form-wa" class="btn btn--wa" href="#" target="_blank" rel="noopener" hidden>%(chat)s Lanjutkan via WhatsApp</a>
      </form>
    </div>
  </div>

  <div class="container">
    <div class="map-wrap reveal">
      <iframe title="Peta lokasi kantor pusat JGS" src="%(maps)s" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      <div class="map-actions"><span>%(addr1)s</span><a class="link-arrow" href="%(maplink)s" target="_blank" rel="noopener">Buka di Google Maps %(arrowi)s</a></div>
    </div>
  </div>
</section>
""" % dict(
        pin=icon("pin"), phone=icon("phone"), arrow=icon("arrow"), arrowi=icon("arrow"), chat=icon("chat"),
        addr="<br>".join(e(x) for x in S["address_lines"][1:]), tel=S["phone_tel"], phoned=S["phone_display"], domain=S["domain"], wa=S["wa"],
        opts=opts, maps=maps, maplink=maps_link, addr1=e(", ".join(S["address_lines"][1:])),
    )
    return "contact.html", head("Kontak", "Hubungi Jagaraya Global Services: alamat kantor pusat Eastpark Apartemen Tower A R.1206, Cakung, Jakarta Timur. Telepon +62 816 111 6375.", root, "contact.html") + header(root, "contact") + body + footer(root)


def page_admin():
    root = "../"
    feats = ["Teks &amp; gambar", "Halaman &amp; section", "Layanan", "Business Focus", "Klien &amp; portofolio", "Berita &amp; aktivitas", "Navigasi", "Warna, font &amp; desain", "Informasi kontak", "SEO", "Media Library"]
    lis = "".join("<li>%s</li>" % f for f in feats)
    return "admin/index.html", """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Admin Panel | JGS</title>
<link rel="icon" type="image/png" href="../assets/images/logo/favicon.png">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Playfair+Display:wght@600;700&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/tokens.css">
<link rel="stylesheet" href="../assets/css/base.css">
<link rel="stylesheet" href="../assets/css/components.css">
<link rel="stylesheet" href="../assets/css/pages.css">
</head>
<body class="admin-body">
<main class="admin-box">
  %s
  <h1>Admin Panel JGS</h1>
  <p>Halaman ini adalah placeholder. Admin Panel akan dibangun pada tahap berikutnya dengan Cloudflare Pages Functions, D1, dan R2, dengan autentikasi yang aman.</p>
  <p style="margin-bottom:0"><strong style="color:#fff">Rencana modul pengelolaan:</strong></p>
  <ul class="admin-list">%s</ul>
  <a class="btn btn--primary" href="../index.html">Kembali ke Website</a>
</main>
</body>
</html>
""" % (img("logo/jgs-shield.png", "Logo JGS", root, loading="eager"), lis)


def main():
    pages = [page_home(), page_about(), page_services(), page_business(), page_clients(), page_contact(), page_admin()]
    for name, content in pages:
        path = os.path.join(PUBLIC, name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("ditulis:", os.path.relpath(path, os.path.dirname(HERE)), "(%d byte)" % len(content.encode("utf-8")))


if __name__ == "__main__":
    main()
