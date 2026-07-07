import sqlite3

def lihat_pesan():

    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM PESAN")

    data = cursor.fetchall()

    if len(data) == 0:
        print("\nBelum ada pesan.")
    else:
        print("\n===== DAFTAR PESAN =====")

        for pesan in data:
            print("-----------------------------")
            print("ID Pesan :", pesan[0])
            print("ID Pengguna :", pesan[1])
            print("Isi Pesan :", pesan[2])
            print("Tanggal :", pesan[3])
            print("Status :", pesan[4])

    conn.close()


def ubah_status():

    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()

    id_pesan = input("\nMasukkan ID Pesan : ")

    print("1. Disetujui")
    print("2. Ditolak")

    pilihan = input("Pilih : ")

    if pilihan == "1":
        status = "Disetujui"

    elif pilihan == "2":
        status = "Ditolak"

    else:
        print("Pilihan tidak valid.")
        conn.close()
        return

    cursor.execute("""
    UPDATE PESAN
    SET status = ?
    WHERE id_pesan = ?
    """,(status,id_pesan))

    conn.commit()

    print("Status berhasil diperbarui.")

    conn.close()


def hapus_pesan():

    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()

    id_pesan = input("\nMasukkan ID Pesan yang akan dihapus : ")

    cursor.execute("""
    DELETE FROM PESAN
    WHERE id_pesan = ?
    """,(id_pesan,))

    conn.commit()

    print("Pesan berhasil dihapus.")

    conn.close()


def menu_moderasi():

    while True:

        print("\n===== MENU MODERASI =====")
        print("1. Lihat Pesan")
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