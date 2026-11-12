# -*- coding: utf-8 -*-
"""
Pemuat konten website JGS (Bahasa Indonesia).

Seluruh teks & foto website dibaca dari folder content/*.json. File-file itu diedit lewat
Admin Decap CMS di /admin/ (setiap penyimpanan = satu commit di GitHub), lalu tools/build.py
menyusun ulang halaman HTML saat deploy di Cloudflare Pages.

Kode ini hanya MEMBACA & MEMERIKSA konten. Jika ada file rusak/kurang, build berhenti dengan
pesan yang jelas, sehingga website yang sedang live tidak berubah.
"""
import datetime
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(ROOT, "content")


class ContentError(Exception):
    pass


def _read(rel):
    path = os.path.join(CONTENT_DIR, rel)
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise ContentError("File konten tidak ditemukan: content/%s" % rel)
    except ValueError as err:
        raise ContentError("File content/%s bukan JSON yang valid: %s" % (rel, err))
    if not isinstance(data, dict):
        raise ContentError("File content/%s harus berupa objek JSON." % rel)
    return data


def _need(data, keys, where):
    missing = [k for k in keys if k not in data]
    if missing:
        raise ContentError("content/%s: kolom wajib hilang: %s" % (where, ", ".join(missing)))


SITE = _read("site.json")
HOME = _read("home.json")
ABOUT_PAGE = _read("about.json")
SERVICES_PAGE = _read("services.json")
BUSINESS_PAGE = _read("business.json")
CLIENTS_PAGE = _read("clients.json")
CONTACT_PAGE = _read("contact.json")
NEWS_PAGE = _read("news_page.json")

_need(SITE, ["name", "short", "tagline", "domain", "url", "phone_display", "phone_tel", "wa", "address_lines",
             "map_query", "cta_title", "cta_text", "footer_description", "footer_note"], "site.json")
_need(HOME, ["meta_description", "hero_before", "hero_em", "hero_after", "hero_lead", "hero_person_1", "hero_person_2",
             "profile_eyebrow", "profile_title", "profile_image", "services_eyebrow", "services_title", "services_lead",
             "sectors_eyebrow", "sectors_title", "sectors_lead", "why_eyebrow", "why_title", "why_items",
             "addvalue_eyebrow", "addvalue_title", "addvalue_lead", "clients_eyebrow", "clients_title", "clients_lead",
             "contact_eyebrow", "contact_title"], "home.json")
_need(ABOUT_PAGE, ["meta_description", "hero_lead", "profile_eyebrow", "profile_title", "about", "belief", "about_image",
                   "vmv_eyebrow", "vmv_title", "karakter", "visi", "misi", "value", "value_words", "nilai_eyebrow",
                   "nilai_title", "tata_nilai", "four_m", "erp_title", "erp"], "about.json")
_need(SERVICES_PAGE, ["meta_description", "hero_title", "hero_lead", "items"], "services.json")
_need(BUSINESS_PAGE, ["meta_description", "hero_lead", "section_eyebrow", "section_title", "section_lead", "photo_note",
                      "sectors", "addvalue_eyebrow", "addvalue_title", "addvalue_lead", "add_value_jgs",
                      "add_value_ops", "key_benefit"], "business.json")
_need(CLIENTS_PAGE, ["meta_description", "hero_title", "hero_lead", "section_eyebrow", "section_title", "clients",
                     "placeholders", "notice", "portfolio_eyebrow", "portfolio_title", "portfolio_lead",
                     "portfolio_items"], "clients.json")
_need(CONTACT_PAGE, ["meta_description", "hero_title", "hero_lead", "info_title", "form_title", "form_notice"], "contact.json")
_need(NEWS_PAGE, ["nav_label", "meta_description", "hero_title", "hero_lead"], "news_page.json")

if len(ABOUT_PAGE["about"]) < 2:
    raise ContentError("content/about.json: 'about' harus berisi 2 paragraf.")
if len(SITE["address_lines"]) < 2:
    raise ContentError("content/site.json: 'address_lines' minimal 2 baris (judul + alamat).")

# ---- bentuk yang dipakai tools/build.py ----
ABOUT = ABOUT_PAGE["about"]
ABOUT_BELIEF = ABOUT_PAGE["belief"]
VISI, MISI, VALUE = ABOUT_PAGE["visi"], ABOUT_PAGE["misi"], ABOUT_PAGE["value"]
VALUE_WORDS = ABOUT_PAGE["value_words"]
TATA_NILAI, ERP = ABOUT_PAGE["tata_nilai"], ABOUT_PAGE["erp"]
FOUR_M = [(x["title"], x["text"], x["icon"]) for x in ABOUT_PAGE["four_m"]]

SERVICES = []
for _i, _s in enumerate(SERVICES_PAGE["items"], 1):
    _need(_s, ["id", "name", "icon", "img", "mode", "short", "long"], "services.json (layanan #%d)" % _i)
    _s = dict(_s)
    _s["subs"] = [(x["title"], x["text"]) for x in _s.get("subs", [])]
    _s["chips"] = list(_s.get("chips", []))
    _s["extra_imgs"] = list(_s.get("extra_imgs", []))
    SERVICES.append(_s)
_ids = [s["id"] for s in SERVICES]
if len(set(_ids)) != len(_ids):
    raise ContentError("content/services.json: ada layanan dengan 'id' kembar: %s" % sorted({i for i in _ids if _ids.count(i) > 1}))

SECTORS = BUSINESS_PAGE["sectors"]
ADD_VALUE_JGS = [(x["title"], x["icon"]) for x in BUSINESS_PAGE["add_value_jgs"]]
ADD_VALUE_OPS = [(x["title"], x["icon"]) for x in BUSINESS_PAGE["add_value_ops"]]
KEY_BENEFIT = BUSINESS_PAGE["key_benefit"]
CLIENTS = CLIENTS_PAGE["clients"]
CLIENT_PLACEHOLDERS = int(CLIENTS_PAGE["placeholders"])

# ---- berita & aktivitas: content/news/*.json (1 file = 1 artikel) ----
NEWS = []
_news_dir = os.path.join(CONTENT_DIR, "news")
if os.path.isdir(_news_dir):
    for _fn in sorted(os.listdir(_news_dir)):
        if not _fn.endswith(".json"):
            continue
        _a = _read(os.path.join("news", _fn))
        _need(_a, ["title", "date"], "news/" + _fn)
        if _a.get("published", True) is False:
            continue
        try:
            _d = datetime.date.fromisoformat(str(_a["date"])[:10])
        except ValueError:
            raise ContentError("content/news/%s: tanggal tidak valid: %r (pakai format TAHUN-BULAN-TANGGAL)" % (_fn, _a["date"]))
        NEWS.append({
            "slug": _fn[:-5], "title": str(_a["title"]).strip(), "date": _d,
            "summary": str(_a.get("summary", "") or "").strip(),
            "image": str(_a.get("image", "") or "").strip(),
            "body": str(_a.get("body", "") or ""),
        })
    NEWS.sort(key=lambda a: (a["date"], a["slug"]), reverse=True)

NAV = [
    ("index.html", "Beranda", "home"),
    ("about.html", "Tentang Kami", "about"),
    ("services.html", "Layanan", "services"),
    ("business-focus.html", "Fokus Bisnis", "business"),
    ("clients.html", "Klien", "clients"),
    ("contact.html", "Kontak", "contact"),
]
if NEWS:  # menu "Berita" hanya muncul bila ada artikel
    NAV.insert(-1, ("news.html", NEWS_PAGE["nav_label"], "news"))
