import sqlite3

def lihat_pesan():
    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id_pesan, isi_pesan FROM PESAN WHERE status='Disetujui'")
    data = cursor.fetchall()

    if len(data) == 0:
        print("\nBelum ada pesan yang disetujui oleh Admin.")
    else:
        print("\n===== DAFTAR PESAN FORUM =====")
        for pesan in data:
            print("ID Pesan :", pesan[0])
            print("Pesan    :", pesan[1])
            print("----------------------")
    conn.close()

def tambah_tanggapan():
    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()

    print("\n--- TAMBAH TANGGAPAN ---")
    id_tanggapan = input("Buat ID Tanggapan baru (contoh: T1, T2): ")
    id_pesan = input("Masukkan ID Pesan yang ingin ditanggapi: ")
    id_pengguna = input("Masukkan ID Pengguna Anda: ")
    isi = input("Masukkan isi tanggapan: ")
    tanggal = input("Masukkan tanggal hari ini (YYYY-MM-DD): ")

    try:
        cursor.execute("""
        INSERT INTO TANGGAPAN (id_tanggapan, id_pesan, id_pengguna, isi_tanggapan, tanggal_tanggapan)
        VALUES (?, ?, ?, ?, ?)
        """, (id_tanggapan, id_pesan, id_pengguna, isi, tanggal))
        conn.commit()
        print("Tanggapan berhasil ditambahkan.")
    except sqlite3.IntegrityError:
        print("Error: ID Tanggapan sudah ada atau ID Pesan tidak ditemukan!")
        
    conn.close()

def lihat_tanggapan():
    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id_tanggapan, id_pesan, isi_tanggapan, tanggal_tanggapan FROM TANGGAPAN")
    data = cursor.fetchall()

    if len(data) == 0:
        print("\nBelum ada tanggapan.")
    else:
        print("\n===== DAFTAR TANGGAPAN =====")
        for t in data:
            print("ID Tanggapan :", t[0])
            print("ID Pesan     :", t[1])
            print("Isi Tanggapan:", t[2])
            print("Tanggal      :", t[3])
            print("------------------")
    conn.close()

def edit_tanggapan():
    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()
    id_tang = input("Masukkan ID Tanggapan yang ingin diubah: ")
    isi = input("Masukkan isi tanggapan baru: ")

    cursor.execute("UPDATE TANGGAPAN SET isi_tanggapan=? WHERE id_tanggapan=?", (isi, id_tang))
    conn.commit()
    print("Tanggapan berhasil diubah.")
    conn.close()

def hapus_tanggapan():
    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()
    id_tang = input("Masukkan ID Tanggapan yang ingin dihapus: ")

    cursor.execute("DELETE FROM TANGGAPAN WHERE id_tanggapan=?", (id_tang,))
    conn.commit()
    print("Tanggapan berhasil dihapus.")
    conn.close()

def menu_respon():
    while True:
        print("\n===== MENU UTAMA RESPONDEN =====")
        print("1. Lihat Pesan")
        print("2. Tambah Tanggapan")
        print("3. Lihat Tanggapan")
        print("4. Edit Tanggapan")
        print("5. Hapus Tanggapan")
        print("6. Kembali")

        pilihan = input("Pilih menu : ")
        if pilihan == "1": lihat_pesan()
        elif pilihan == "2": tambah_tanggapan()
        elif pilihan == "3": lihat_tanggapan()
        elif pilihan == "4": edit_tanggapan()
        elif pilihan == "5": hapus_tanggapan()
        elif pilihan == "6": break
        else: print("Pilihan tidak tersedia.")