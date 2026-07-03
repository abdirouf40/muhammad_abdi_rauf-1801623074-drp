from datetime import datetime

# ==========================================
# SIMULASI DUMMY FUNGSI PENYIMPANAN
# (Ganti/sesuaikan dengan import aslimu)
# ==========================================
def muat_data():
    # Simulasi struktur data ekspor dari aktivasi.py
    return {
        "pesan": [
            {"id_pesan": 1, "id_pengguna": 101, "isi_pesan": "Halo, ini pesan pertama!", "tanggal_kirim": "2026-07-03 15:00:00", "status": "aktif"}
        ],
        "tanggapan": [
            {"id_tanggapan": 1, "id_pesan": 1, "id_pengguna": 102, "isi_tanggapan": "Respon pertama nih.", "tanggal_tanggapan": "2026-07-03 15:05:00"}
        ]
    }

def simpan_data(data):
    print("-> [INFO] Data berhasil disimpan ke file JSON!")

# ==========================================
# FUNGSI UTAMA (CRUD SESUAI ERD)
# ==========================================

def tampilkan_menu():
    print("\n=== FORUM PESAN ANONIM (Respon) ===")
    print("1. Lihat semua pesan & respon")
    print("2. Beri respon ke sebuah pesan")
    print("3. Edit respon")
    print("4. Hapus respon")
    print("5. Keluar")

def lihat_pesan(data):
    """READ: Menampilkan pesan dan tanggapannya sesuai ERD"""
    if not data.get("pesan"):
        print("Belum ada pesan di forum.")
        return

    print("\n--- DAFTAR PESAN ---")
    for pesan in data["pesan"]:
        # Cetak detail pesan (menggunakan nama kolom di ERD)
        print(f"\n[ID Pesan: {pesan['id_pesan']}] ({pesan['tanggal_kirim']})")
        print(f"Isi: \"{pesan['isi_pesan']}\"")
        print("Tanggapan:")

        # Cari tanggapan yang punya 'id_pesan' yang sama (Simulasi Relasi ERD)
        ada_tanggapan = False
        for tg in data.get("tanggapan", []):
            if tg["id_pesan"] == pesan["id_pesan"]:
                print(f"  -> [ID Respon: {tg['id_tanggapan']}] {tg['isi_tanggapan']}")
                ada_tanggapan = True
        
        if not ada_tanggapan:
            print("  (belum ada tanggapan)")

def buat_respon(data):
    """CREATE: Menambahkan tanggapan baru ke tabel TANGGAPAN"""
    lihat_pesan(data)
    
    try:
        id_pesan_target = int(input("\nMasukkan ID pesan yang mau direspon: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    # Cek apakah ID pesan tersebut memang ada
    pesan_ditemukan = False
    for pesan in data["pesan"]:
        if pesan["id_pesan"] == id_pesan_target:
            pesan_ditemukan = True
            break
            
    if not pesan_ditemukan:
        print("ID pesan tidak ditemukan.")
        return

    isi = input("Tulis respon anonim kamu: ").strip()
    if not isi:
        print("Respon tidak boleh kosong.")
        return

    # Membuat ID tanggapan baru secara otomatis (hitung jumlah + 1)
    id_tanggapan_baru = len(data["tanggapan"]) + 1

    # Struktur data baru, 100% mengikuti atribut tabel TANGGAPAN di ERD
    respon_baru = {
        "id_tanggapan": id_tanggapan_baru,
        "id_pesan": id_pesan_target,
        "id_pengguna": 999,  # Contoh dummy ID Pengguna anonim
        "isi_tanggapan": isi,
        "tanggal_tanggapan": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Dimasukkan ke list tanggapan utama (bukan di dalam pesannya)
    data["tanggapan"].append(respon_baru)
    simpan_data(data)
    print(f"Respon terkirim! (ID Respon baru: {id_tanggapan_baru})")

def edit_respon(data):
    """UPDATE: Mengubah isi tanggapan berdasarkan ID Tanggapan"""
    try:
        id_tg_target = int(input("\nMasukkan ID Respon yang mau diedit: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    # Cari tanggapannya di dalam list tanggapan
    for tg in data["tanggapan"]:
        if tg["id_tanggapan"] == id_tg_target:
            isi_baru = input(f"Isi sekarang: {tg['isi_tanggapan']}\nIsi baru: ").strip()
            if isi_baru:
                tg["isi_tanggapan"] = isi_baru
                simpan_data(data)
                print("Respon berhasil diperbarui.")
                return
            else:
                print("Isi baru tidak boleh kosong, dibatalkan.")
                return

    print("ID Respon tidak ditemukan.")

def hapus_respon(data):
    """DELETE: Menghapus tanggapan dari list berdasarkan ID Tanggapan"""
    try:
        id_tg_target = int(input("\nMasukkan ID Respon yang mau dihapus: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    # Cari dan hapus tanggapannya
    for tg in data["tanggapan"]:
        if tg["id_tanggapan"] == id_tg_target:
            konfirmasi = input(f"Yakin hapus respon ID {id_tg_target}? (y/n): ").lower()
            if konfirmasi == 'y':
                data["tanggapan"].remove(tg)
                simpan_data(data)
                print("Respon berhasil dihapus.")
                return
            else:
                print("Dibatalkan.")
                return

    print("ID Respon tidak ditemukan.")

# ==========================================
# MENU UTAMA
# ==========================================
def main():
    data = muat_data()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            lihat_pesan(data)
        elif pilihan == "2":
            buat_respon(data)
        elif pilihan == "3":
            edit_respon(data)
        elif pilihan == "4":
            hapus_respon(data)
        elif pilihan == "5":
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
    