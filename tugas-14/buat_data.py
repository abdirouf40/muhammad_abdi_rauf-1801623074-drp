import json
import random
from datetime import datetime, timedelta

def generate_dummy_3mb():
    kategori_sampel = {
        "Asmara": [
            "Kenapa ya dia tiba-tiba berubah, padahal kemarin masih baik-baik aja. Capek batin banget.",
            "Udah pacaran 5 tahun tapi ujung-ujungnya ditinggal nikah, nyesek banget rasanya.",
            "LDR bener-bener menguji kepercayaan, kadang suka overthinking sendiri malam-malam."
        ],
        "Karir & Keuangan": [
            "Pengen resign tapi cicilan masih banyak, bertahan di tempat toxic bener-bener menguji mental.",
            "Kerja keras bagai kuda tapi gaji gak seberapa, cuma cukup buat bayar kosan sama makan.",
            "Udah kirim ratusan lamaran kerja tapi belum ada yang panggil, rasanya pengen menyerah."
        ],
        "Pendidikan": [
            "Stres kuliah semester ini berat banget, pengen nangis rasanya pas liat tugas project coding.",
            "Sedih banget hari ini, mana tugas numpuk belum selesai ditambah revisi terus dari dosen.",
            "Overthinking tiap malam mikirin masa depan nanti bakal jadi apa setelah lulus kuliah."
        ],
        "Kehidupan Sehari-hari": [
            "Alhamdulillah hari ini dapet rezeki nomplok, setidaknya ada alasan buat tersenyum.",
            "Butuh temen ngobrol, sepi banget hidup di perantauan sendirian gini.",
            "Hari ini apes banget, dompet hilang pas lagi buru-buru naik angkutan umum."
        ]
    }
    
    status_pilihan = ["Disetujui", "Ditolak", "Pending"]
    list_pesan = []
    
    print("Sedang membuat data dummy 3 MB sesuai kebutuhan tugas...")
    
    for i in range(1, 13501):
        kategori_acak = random.choice(list(kategori_sampel.keys()))
        pesan_acak = random.choice(kategori_sampel[kategori_acak])
        
        status_acak = random.choice(status_pilihan)
        id_user_acak = str(random.randint(100, 999))
        views_acak = random.randint(10, 500)
        
        waktu_acak = datetime.now() - timedelta(minutes=random.randint(1, 50000))
        str_tanggal = waktu_acak.strftime("%Y-%m-%d %H:%M:%S")
        
        list_pesan.append({
            "id_pesan": str(i),
            "id_pengguna": id_user_acak,
            "isi_pesan": pesan_acak,
            "tanggal_kirim": str_tanggal,
            "status": status_acak,
            "kategori": kategori_acak,
            "jumlah_views": views_acak
        })
        
    data_gabungan = {
        "pengguna": [
            {"id_pengguna": "1", "username": "admin", "email": "admin@forum.com", "password": "admin"}
        ],
        "pesan": list_pesan,
        "tanggapan": []
    }
    
    with open('forum_curhat_dummy.json', 'w', encoding='utf-8') as f:
        json.dump(data_gabungan, f, indent=4)
        
    print("✓ Sukses! File 'forum_curhat_dummy.json' bertema Pesan Sesuai ERD berhasil dibuat (> 3 MB).")

if __name__ == "__main__":
    generate_dummy_3mb()