# -*- coding: utf-8 -*-
"""
Konten website JGS - Bahasa Indonesia.
Sumber: Company Profile JGS 2025 (kesalahan penulisan sudah dikoreksi tanpa mengubah makna).

Untuk menambah Bahasa Inggris: salin file ini menjadi content_en.py, terjemahkan
nilainya (jangan ubah nama kunci), lalu daftarkan di tools/build.py (LANGS).
"""

SITE = {
    "name": "JAGARAYA GLOBAL SERVICES",
    "short": "JGS",
    "tagline": "FACILITY SERVICE SOLUTION",
    "domain": "www.jagaraya.id",
    "url": "https://www.jagaraya.id",
    "phone_display": "+62 816 111 6375",
    "phone_tel": "+628161116375",
    "wa": "628161116375",
    "address_lines": ["Head Office", "Eastpark Apartemen Tower A R.1206", "KRT Radjiman – Cakung", "Jakarta Timur – Indonesia"],
    "map_query": "Eastpark Apartemen Cakung Jakarta Timur",
}

NAV = [
    ("index.html", "Beranda", "home"),
    ("about.html", "Tentang Kami", "about"),
    ("services.html", "Layanan", "services"),
    ("business-focus.html", "Fokus Bisnis", "business"),
    ("clients.html", "Klien", "clients"),
    ("contact.html", "Kontak", "contact"),
]

ABOUT = [
    "JAGARAYA GLOBAL SERVICES (JGS) adalah perusahaan yang berfokus pada penyediaan sumber daya manusia berkualitas tinggi, baik untuk dipekerjakan langsung oleh pelanggan maupun melalui sistem alihdaya, yang dilengkapi dengan keahlian, kompetensi, integritas, dan pengetahuan yang komprehensif dalam memenuhi kebutuhan seluruh klien kami yang berasal dari berbagai sektor industri bisnis.",
    "JGS merupakan bagian dari Jagaraya Group, dengan pengembangan bisnis di berbagai bidang usaha yang terus berjalan dalam memperkuat bisnis group secara luas dengan skala nasional dan internasional.",
]
ABOUT_BELIEF = "Kami percaya bahwa kunci untuk memberikan pelayanan kelas utama adalah investasi pada sumber daya manusia. Oleh karena itu, kami memberikan kontribusi yang signifikan dalam hal perekrutan, pelatihan, dan pengembangan keterampilan, serta terus melakukan inovasi dalam pengembangan bakat dan profesionalisme setiap karyawan untuk mencapai tingkat motivasi terbaik, semuanya untuk mencapai kepuasan klien."

VISI = "Menjadi perusahaan terbaik di bidang alihdaya dan mitra yang dapat diandalkan bagi seluruh klien kami di berbagai bidang industri."
MISI = "Menyampaikan pelayanan kelas terbaik dengan dukungan tenaga kerja yang terampil dan profesional di setiap bidang sektor industri serta pendekatan yang terstruktur dalam menjalankan bisnis perusahaan."
VALUE = "Profesional, dedikasi dan performa tinggi serta integritas bersama untuk mencapai tujuan kepuasan klien."
VALUE_WORDS = ["Profesional", "Dedikasi", "Performa Tinggi", "Integritas"]

TATA_NILAI = "Dengan manajemen yang solid dan kokoh, dukungan sumber daya manusia yang terdidik, terlatih dan profesional, kekuatan finansial, serta metode kerja yang tertata (Man – Money – Method & Materials), Jagaraya Global Services (JGS) dapat bersaing dalam industri facility service dan jasa keamanan di Indonesia."
ERP = "Sistem ERP (Enterprise Resources Planning) yang efisien dan efektif dalam pengelolaan operasional secara sistematis merupakan keunggulan kami, dengan tujuan meningkatkan kinerja manajemen dalam memberikan pelayanan terbaik bagi pengguna jasa."

FOUR_M = [
    ("Man", "Sumber daya manusia yang terdidik, terlatih, dan profesional.", "users"),
    ("Money", "Kekuatan finansial yang mendukung keberlangsungan layanan.", "chart"),
    ("Method", "Metode kerja yang tertata dan terstruktur.", "doc"),
    ("Materials", "Dukungan peralatan dan perlengkapan sesuai kebutuhan layanan.", "box"),
]

# slug, nama, ikon, gambar (None = hanya ikon), mode gambar (cover/cutout), deskripsi singkat, deskripsi lengkap (paragraf)
SERVICES = [
    {
        "id": "security", "name": "Jagaraya Security Service", "icon": "shield",
        "img": "general/guard-2.png", "mode": "cutout",
        "short": "Layanan keamanan aset perusahaan maupun pribadi dengan tenaga satuan pengamanan yang profesional.",
        "long": [
            "Keamanan dan kenyamanan merupakan pilihan mutlak bagi setiap manusia dan dunia usaha. Meningkatnya mobilitas suatu perusahaan membutuhkan ketepatan pengelolaan SDM secara efisien dan efektif.",
            "Jagaraya Security Service hadir memberikan pelayanan keamanan aset perusahaan maupun pribadi pengguna jasa, dengan tetap menjaga komitmen kepercayaan klien. Dengan SDM tenaga satuan pengamanan yang profesional, berkomitmen dan berkualitas, kami hadirkan pelayanan terbaik bagi pengguna jasa.",
        ],
    },
    {
        "id": "housekeeping", "name": "Jagaraya House Keeping", "icon": "sparkle",
        "img": "general/housekeeping.jpg", "mode": "contain",
        "short": "“Clean, Health & Safety” — penanganan kebersihan indoor maupun outdoor, lengkap dengan SOP dan pelaporan.",
        "long": [
            "“Clean, Health & Safety” adalah motto kami. Jagaraya House Keeping senantiasa menjaga agar lingkungan selalu bersih, sehat dan aman, baik secara mental maupun jasmani, sekaligus berusaha menciptakan nilai bersih bagi lingkungan tempat kami berada.",
            "Tugas kami adalah menangani seluruh masalah kebersihan indoor maupun outdoor, dimulai dari penyediaan tenaga kerja, pelatihan dan pengetahuan tentang kebersihan, SOP (Standard Operating Procedure) yang disesuaikan dengan tempat kami bekerja, hingga pengawasan berkala dan pelaporan. Totalitas kami dalam bekerja menjadi modal awal untuk memberikan pelayanan terbaik bagi klien.",
        ],
    },
    {
        "id": "hr", "name": "Jagaraya HR Provider", "icon": "users",
        "img": "services/hr-reception.jpg", "mode": "cover",
        "short": "Solusi kebutuhan tenaga kerja yang tepat, profesional, dan berkualitas melalui sistem perekrutan yang handal.",
        "long": [
            "Solusi kebutuhan tenaga kerja yang tepat, profesional dan berkualitas ada pada Jagaraya HR Provider, melalui sistem perekrutan yang handal, cepat dan tepat guna untuk menjadi tenaga profesional sesuai kebutuhan klien.",
            "Program CMC diberikan untuk mengoptimalkan potensi tenaga kerja sehingga menjadi tenaga kerja yang ahli dan bermotivasi tinggi. Pelayanan “The Right Man with The Right Job on The Right Place” adalah fokus utama kami.",
        ],
    },
    {
        "id": "parking", "name": "Jagaraya Parking Management", "icon": "parking",
        "img": "services/parking-valet.jpeg", "mode": "cover",
        "short": "Pengelolaan perparkiran dengan tenaga profesional berpengalaman dan dukungan teknologi perparkiran terkini.",
        "long": [
            "Kebutuhan parkir serta fasilitas penunjang mendorong kami menghadirkan Jagaraya Parking Management dengan tenaga profesional yang berpengalaman dan didukung teknologi perparkiran terkini.",
            "Kami memberikan pelayanan prima demi tercapainya kepuasan pengguna jasa, menjadikan kami pilihan tepat untuk solusi perparkiran properti klien.",
        ],
    },
    {
        "id": "pest", "name": "Jagaraya Pest Control Service", "icon": "bug",
        "img": "services/pest-control.png", "mode": "cover",
        "short": "Solusi kebersihan ruangan (higienis) dari serangga dan disinfektan, dengan peralatan lengkap dan SDM terlatih.",
        "long": [
            "Solusi kebutuhan penanganan kebersihan ruangan (higienis) dari serangga dan disinfektan lainnya. Jagaraya Pest Control Service hadir memenuhi kebutuhan Anda dengan peralatan lengkap, SDM terlatih dan profesional, efisien dan efektif, serta cepat dan handal dalam pengelolaannya.",
        ],
    },
    {
        "id": "safety", "name": "Jagaraya Security System & Safety", "icon": "camera",
        "img": "services/cctv.jpeg", "mode": "contain",
        "short": "Instalasi sistem keamanan: alarm, CCTV, access control, fire extinguisher, fire alarm, dan lainnya.",
        "long": [
            "Kami siap memberikan pelayanan dalam instalasi security system, alarm, CCTV, access control, fire extinguisher, fire alarm, dan lainnya.",
            "Pentingnya sistem keamanan internal yang terintegrasi dengan informasi dan teknologi, serta SDM yang terlatih dan profesional, sangat mendukung pengembangan bisnis klien dan terjaminnya keamanan secara menyeluruh.",
        ],
        "chips": ["Alarm", "CCTV", "Access Control", "Fire Extinguisher", "Fire Alarm"],
        "extra_imgs": ["services/access-control.jpeg", "services/fire-extinguisher.png"],
    },
    {
        "id": "transport", "name": "Jagaraya Transportation & Logistic", "icon": "truck",
        "img": "services/transport-2.jpeg", "mode": "cover",
        "short": "Layanan logistik dan transportasi dengan kombinasi sistem IT dan harga yang kompetitif, berlandaskan Kaizen Spirit.",
        "long": [
            "Jagaraya Group melalui jaringan usaha Jagaraya Transportation & Logistic memiliki misi menjadi bagian perusahaan logistik dan transportasi besar di Indonesia.",
            "Kami menyediakan pelayanan logistik dan transportasi dengan kombinasi sistem IT serta harga yang kompetitif, mempertahankan “Kaizen Spirit” dengan selalu melakukan perubahan (inovasi) untuk menjadi lebih baik dalam layanan operasional kami.",
        ],
        "extra_imgs": ["services/transport-1.png", "services/transport-3.jpeg"],
    },
    {
        "id": "waste", "name": "Jagaraya Waste Management Service", "icon": "leaf",
        "img": "services/waste-icons.jpeg", "mode": "cover",
        "short": "Reduce – Reuse – Recycle: pengangkutan sampah, daur ulang, pengolahan air limbah, dan limbah B3.",
        "long": [
            "Reduce – Reuse – Recycle. Layanan trash pick up & recycling untuk perusahaan, acara, gedung, pabrik, hunian, dan lainnya.",
        ],
        "subs": [
            ("Pengolahan Air Limbah", "Menyediakan jasa pengolahan air limbah industri yang telah digunakan untuk mengubah air limbah menjadi air yang dapat digunakan kembali. Prosesnya berlangsung di instalasi pengolahan air limbah (IPAL) sehingga polutan dalam air limbah industri dapat dihilangkan atau dihancurkan. Bersama Wastec International, dampak lingkungan dapat diminimalisir."),
            ("Pengolahan Limbah B3", "Menyediakan jasa pengangkutan, pengolahan dan pengumpulan untuk limbah B3 industri dan medis, serta dapat mengolah hampir semua fase limbah mulai dari fase solid, liquid, dan sludge, demi lingkungan yang sehat dan bebas dari pencemaran."),
        ],
    },
]

SECTORS = [
    ("Office Building", "Gedung perkantoran", "building"),
    ("Banks", "Perbankan", "bank"),
    ("Industrial Plant", "Pabrik dan kawasan industri", "factory"),
    ("Logistic & Retail", "Logistik dan ritel", "box"),
    ("Hospital", "Rumah sakit", "hospital"),
    ("Apartment & Residences", "Apartemen dan hunian", "home"),
    ("Hotel, Café & Restaurant", "Perhotelan, kafe, dan restoran", "bed"),
    ("Mall & Marketplace", "Pusat perbelanjaan dan pasar", "bag"),
    ("School & Campus", "Sekolah dan kampus", "cap"),
]

ADD_VALUE_JGS = [
    ("Business Process", "layers"), ("Service Level Agreement (SLA)", "doc"), ("Key Performance Indicator (KPI)", "target"),
]
ADD_VALUE_OPS = [
    ("Operation Management", "cog"), ("Administration", "doc"), ("Knowledge Management", "eye"),
    ("Reporting", "chart"), ("Quality Management", "check"), ("Resource Management", "users"), ("Infrastructure", "server"),
]
KEY_BENEFIT = [
    "Metode andal kami berbasis Man, Money, Method & Materials.",
    "Klien dapat mengalokasikan lebih banyak fokus pada bisnis inti perusahaan untuk mencapai target.",
    "Pengalihan risiko kepada perusahaan alihdaya.",
    "Pengendalian pelaksanaan layanan dapat dilakukan melalui SLA/KPI.",
]

# Klien: hanya logo yang tercantum pada Company Profile JGS 2025. Slot lain = placeholder.
CLIENTS = [
    {"name": "Mr. D.I.Y", "img": "clients/mr-diy.png"},
    {"name": "J&T Express", "img": "clients/jnt-express.png"},
    {"name": "ISTN", "img": "clients/istn.png"},
]
CLIENT_PLACEHOLDERS = 6
