import sqlite3

def lihat_pesan():

    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id_pesan, isi_pesan
    FROM PESAN
    WHERE status='Disetujui'
    """)

    data = cursor.fetchall()

    if len(data) == 0:
        print("\nBelum ada pesan.")
    else:

        print("\n===== DAFTAR PESAN =====")

        for pesan in data:

            print("ID :", pesan[0])
            print("Pesan :", pesan[1])
            print("----------------------")

    conn.close()


def tambah_tanggapan():

    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()

    id_pesan = input("Masukkan ID Pesan : ")
    id_pengguna = input("Masukkan ID Pengguna : ")
    isi = input("Masukkan Tanggapan : ")
    tanggal = input("Tanggal : ")

    cursor.execute("""
    INSERT INTO TANGGAPAN
    (id_pesan,id_pengguna,isi_tanggapan,tanggal_tanggapan)
    VALUES (?,?,?,?)
    """,(id_pesan,id_pengguna,isi,tanggal))

    conn.commit()

    print("Tanggapan berhasil ditambahkan.")

    conn.close()


def lihat_tanggapan():

    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM TANGGAPAN
    """)

    data = cursor.fetchall()

    if len(data)==0:

        print("\nBelum ada tanggapan.")

    else:

        print("\n===== TANGGAPAN =====")

        for t in data:

            print("ID :",t[0])
            print("ID Pesan :",t[1])
            print("ID Pengguna :",t[2])
            print("Isi :",t[3])
            print("Tanggal :",t[4])
            print("------------------")

    conn.close()


def edit_tanggapan():

    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()

    id = input("ID Tanggapan : ")
    isi = input("Isi baru : ")

    cursor.execute("""
    UPDATE TANGGAPAN
    SET isi_tanggapan=?
    WHERE id_tanggapan=?
    """,(isi,id))

    conn.commit()

    print("Tanggapan berhasil diubah.")

    conn.close()


def hapus_tanggapan():

    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()

    id = input("ID Tanggapan : ")

    cursor.execute("""
    DELETE FROM TANGGAPAN
    WHERE id_tanggapan=?
    """,(id,))

    conn.commit()

    print("Tanggapan berhasil dihapus.")

    conn.close()


def menu_respon():

    while True:

        print("\n===== MENU TANGGAPAN =====")
        print("1. Lihat Pesan")
        print("2. Tambah Tanggapan")
        print("3. Lihat Tanggapan")
        print("4. Edit Tanggapan")
        print("5. Hapus Tanggapan")
        print("6. Kembali")

        pilih = input("Pilih menu : ")

        if pilih=="1":
            lihat_pesan()

        elif pilih=="2":
            tambah_tanggapan()

        elif pilih=="3":
            lihat_tanggapan()

        elif pilih=="4":
            edit_tanggapan()

        elif pilih=="5":
            hapus_tanggapan()

        elif pilih=="6":
            break

        else:
            print("Pilihan tidak tersedia.")