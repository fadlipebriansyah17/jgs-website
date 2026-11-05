# -*- coding: utf-8 -*-
"""
Menghasilkan functions/_lib/default-content.js dan functions/_lib/icons.js dari tools/content_id.py.
Jalankan:  python3 tools/export_seed.py
Isi default ini dipakai Admin Dashboard sebagai titik awal sebelum ada perubahan yang disimpan.
"""
import json, os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import content_id as C
import build

content = {
    "profile": {
        "about": list(C.ABOUT), "belief": C.ABOUT_BELIEF, "visi": C.VISI, "misi": C.MISI,
        "value": C.VALUE, "value_words": list(C.VALUE_WORDS), "tata_nilai": C.TATA_NILAI, "erp": C.ERP,
    },
    "services": [{
        "id": s["id"], "name": s["name"], "icon": s["icon"], "img": s["img"], "mode": s["mode"],
        "short": s["short"], "long": list(s["long"]), "chips": list(s.get("chips", [])),
        "extra_imgs": list(s.get("extra_imgs", [])),
        "subs": [{"title": a, "text": b} for a, b in s.get("subs", [])],
    } for s in C.SERVICES],
    "sectors": [{"name": n, "desc": d, "icon": i, "img": ""} for n, d, i in C.SECTORS],
    "clients": [{"name": c["name"], "img": c["img"]} for c in C.CLIENTS],
    "client_placeholders": C.CLIENT_PLACEHOLDERS,
}
out = os.path.join(ROOT, "functions", "_lib")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "default-content.js"), "w", encoding="utf-8") as f:
    f.write("// DIHASILKAN oleh tools/export_seed.py dari tools/content_id.py. Jangan edit manual.\n")
    f.write("export const DEFAULT_CONTENT = " + json.dumps(content, ensure_ascii=False, indent=2) + ";\n")
with open(os.path.join(out, "icons.js"), "w", encoding="utf-8") as f:
    f.write("// DIHASILKAN oleh tools/export_seed.py dari tools/build.py (ICONS).\n")
    f.write("export const ICON_NAMES = " + json.dumps(list(build.ICONS.keys())) + ";\n")
print("OK:", len(content["services"]), "layanan,", len(content["sectors"]), "sektor,", len(content["clients"]), "klien")
