import sqlite3

def lihat_pesan():
    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id_pesan, isi_pesan, status FROM PESAN")
    data = cursor.fetchall()

    if len(data) == 0:
        print("\nBelum ada pesan yang masuk.")
    else:
        print("\n===== SEMUA PESAN DI DATABASE =====")
        for p in data:
            print(f"ID Pesan: {p[0]} | Isi: {p[1]} | Status: {p[2]}")
            print("-----------------------------------")
    conn.close()

def ubah_status():
    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()
    id_pilih = input("Masukkan ID Pesan yang ingin diubah: ")
    status_baru = input("Ketik status baru ('Disetujui' / 'Ditolak'): ")

    cursor.execute("UPDATE PESAN SET status=? WHERE id_pesan=?", (status_baru, id_pilih))
    conn.commit()
    print(f"Status pesan {id_pilih} berhasil diubah menjadi {status_baru}!")
    conn.close()

def hapus_pesan():
    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()
    id_pilih = input("Masukkan ID Pesan yang ingin dihapus: ")

    cursor.execute("DELETE FROM PESAN WHERE id_pesan=?", (id_pilih,))
    conn.commit()
    print(f"Pesan {id_pilih} berhasil dihapus dari database.")
    conn.close()

def menu_moderasi():
    while True:
        print("\n===== MENU MODERASI PESAN (ADMIN) =====")
        print("1. Lihat Semua Pesan")
        print("2. Ubah Status Pesan")
        print("3. Hapus Pesan")
        print("4. Kembali")
        
        pilihan = input("Pilih menu : ")
        
        if pilihan == "1":
            lihat_pesan()
        elif pilihan == "2":
            ubah_status()
        elif pilihan == "3":
            hapus_pesan()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak tersedia.")