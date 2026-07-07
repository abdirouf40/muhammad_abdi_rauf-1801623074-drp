def kirim_pesan():
    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()

    isi = input("Masukkan pesan: ")

    cursor.execute("""
    INSERT INTO PESAN
    (id_pengguna, isi_pesan, tanggal_kirim, status)
    VALUES (?, ?, ?, ?)
    """,
    (1, isi, datetime.now(), "Pending"))

    conn.commit()
    conn.close()

    print("Pesan berhasil dikirim.")