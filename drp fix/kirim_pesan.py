import sqlite3
from datetime import datetime

def kirim_pesan():
    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()

    print("\n===== MENU KIRIM PESAN =====")
    # Meminta input ID secara manual agar tidak bentrok di database bertipe TEXT
    id_pesan = input("Buat ID Pesan baru (contoh: P1, P2): ")
    isi = input("Masukkan isi pesan: ")

    try:
        cursor.execute("""
        INSERT INTO PESAN (id_pesan, id_pengguna, isi_pesan, tanggal_kirim, status)
        VALUES (?, ?, ?, ?, ?)
        """, (id_pesan, "1", isi, str(datetime.now()), "Pending"))
        
        conn.commit()
        print("Pesan berhasil dikirim dan menunggu moderasi!")
    except sqlite3.IntegrityError:
        print("Error: ID Pesan sudah digunakan. Gunakan ID lain!")
        
    conn.close()