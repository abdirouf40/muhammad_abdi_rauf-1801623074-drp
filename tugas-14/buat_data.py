import json
import random
from datetime import datetime, timedelta

# Contoh potongan kalimat curhat biar datanya kelihatan nyata dan panjang
contoh_curhatan = [
    "Sedih banget hari ini, mana tugas numpuk belum selesai ditambah revisi terus.",
    "Kenapa ya dia tiba-tiba berubah, padahal kemarin masih baik-baik aja. Capek batin.",
    "Pengen resign tapi cicilan masih banyak, bertahan di tempat toxic bener-bener menguji mental.",
    "Hubungan sama orang tua lagi renggang gara-gara masalah sepele, butuh tempat cerita.",
    "Overthinking tiap malam mikirin masa depan nanti bakal jadi apa ya..."
]

# Daftar status sesuai kebutuhan ERD
status_master = ["aktif", "diarsipkan", "dihapus"]

data_curhat = []

print("Sedang membuat data dummy sesuai ERD...")

# Membuat 40.000 data pesan agar ukuran file tembus > 3 MB sesuai syarat tugas
for i in range(1, 40001):
    # Membuat tanggal kirim acak mundur dari waktu sekarang
    waktu_acak = datetime.now() - timedelta(minutes=random.randint(1, 50000))
    str_tanggal = waktu_acak.strftime("%Y-%m-%d %H:%M:%S")

    # Struktur data baru: 100% SAMA DENGAN TABEL PESAN DI ERD KELOMPOK
    pesan = {
        "id_pesan": i,                              # PK di ERD
        "id_pengguna": random.randint(100, 999),    # FK ke tabel PENGGUNA
        "isi_pesan": random.choice(contoh_curhatan),# Atribut isi pesan
        "tanggal_kirim": str_tanggal,               # Atribut tanggal kirim
        "status": random.choice(status_master)      # Atribut status
    }
    
    data_curhat.append(pesan)

# Menyimpan data curhat ke file forum_curhat_dummy.json
with open("forum_curhat_dummy.json", "w") as f:
    json.dump(data_curhat, f, indent=4)

print("✔ Sukses! File 'forum_curhat_dummy.json' bertema Pesan Sesuai ERD berhasil dibuat (> 3 MB).")