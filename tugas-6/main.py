# =========================================================
# Tugas 6: If-Statement (Aplikasi Manajemen Aktivitas)
<<<<<<< HEAD
# Nama: Ayesha Putri Tyaslungit
# NIM: 1801624172
# =========================================================

from datetime import datetime

print("=== APLIKASI MANAJEMEN AKTIVITAS Sederhana ===")

# 1. Meminta input kegiatan dari user
kegiatan = input("Masukkan kegiatan yang akan dilakukan (sarapan/kerja): ").lower().strip()

# 2. Logika utama menggunakan If-Statement
if kegiatan == "sarapan":
    # Jika memilih aktivitas sarapan
    menu = input("Mau sarapan menu apa hari ini? ").lower().strip()
    
    # Cek ketersediaan bahan (telur, ikan, nugget)
    if menu == "telur" or menu == "ikan" or menu == "nugget":
        print(f"\n[HASIL TERMINAL]: Bahan untuk menu '{menu}' tersedia di lokasi Anda.")
        print("Namun, bahan tersebut perlu dimasak terlebih dahulu.")
    else:
        print(f"\n[HASIL TERMINAL]: Bahan untuk menu '{menu}' tidak tersedia.")
        print("Anda harus membeli bahannya terlebih dahulu.")

elif kegiatan == "kerja":
    # Jika memilih aktivitas berangkat kerja
    waktu_sekarang = datetime.now()
    jam_sekarang = waktu_sekarang.hour
    menit_sekarang = waktu_sekarang.minute
    
    print(f"\nWaktu komputer saat ini: {jam_sekarang:02d}:{menit_sekarang:02d}")
    print("Jadwal masuk kerja: 08:00")
    
    # Deteksi keterlambatan (jika sudah jam 8 lewat menit ke-1 atau jam 9 dst)
    if jam_sekarang > 8 or (jam_sekarang == 8 and menit_sekarang > 0):
        print("\n[NOTIFIKASI TERMINAL]: Anda sudah TERLAMBAT masuk kerja!")
    else:
        print("\n[NOTIFIKASI TERMINAL]: Anda BELUM terlambat masuk kerja. Selamat beraktivitas!")

else:
    # Jika menginput kegiatan di luar sarapan atau kerja
    print("\n[HASIL TERMINAL]: Kegiatan tidak dikenali. Silakan pilih 'sarapan' atau 'kerja'.")