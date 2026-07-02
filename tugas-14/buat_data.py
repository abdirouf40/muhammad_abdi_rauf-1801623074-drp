import json
import random

# Daftar kategori curhat yang ada di forum anonim kamu
kategori_master = ["Asmara", "Kuliah/Tugas", "Keluarga", "Karir/Kerjaan", "Kesehatan Mental"]

# Contoh potongan kalimat curhat biar datanya kelihatan nyata dan panjang
contoh_curhatan = [
    "Sedih banget hari ini, mana tugas numpuk belum selesai ditambah revisi terus.",
    "Kenapa ya dia tiba-tiba berubah, padahal kemarin masih baik-baik aja. Capek batin.",
    "Pengen resign tapi cicilan masih banyak, bertahan di tempat toxic bener-bener menguji mental.",
    "Hubungan sama orang tua lagi renggang gara-gara masalah sepele, butuh tempat cerita.",
    "Overthinking tiap malam mikirin masa depan nanti bakal jadi apa ya..."
]

data_curhat = []

# Membuat 40.000 data curhatan agar ukuran file tembus > 3 MB sesuai syarat tugas
for i in range(1, 40001):
    kategori = random.choice(kategori_master)
    postingan = {
        "id_postingan": i,
        "kategori": kategori,
        "isi_curhat": random.choice(contoh_curhatan),
        "jumlah_views": random.randint(100, 5000), # Berapa kali curhatan dibaca (100 - 5000 kali)
        "jumlah_likes": random.randint(5, 500)       # Jumlah likes dari user lain
    }
    data_curhat.append(postingan)

# Menyimpan data curhat ke file forum_curhat_dummy.json
with open("forum_curhat_dummy.json", "w") as f:
    json.dump(data_curhat, f, indent=4)

print("✅ Sukses! File 'forum_curhat_dummy.json' bertema Curhatan berhasil dibuat (> 3 MB).")