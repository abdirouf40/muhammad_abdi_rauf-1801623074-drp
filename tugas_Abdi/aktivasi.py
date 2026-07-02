import sqlite3
import json
import os

# Fungsi untuk menghubungkan ke database
def hit_database():
    # Menghubungkan ke database sqlite
    conn = sqlite3.connect('forum_anonim.db')
    cursor = conn.cursor()
    
    # Membuat tabel otomatis jika belum ada di database ini
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PENGGUNA (
        id_pengguna TEXT PRIMARY KEY,
        username TEXT,
        email TEXT,
        password TEXT
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PESAN (
        id_pesan TEXT PRIMARY KEY,
        id_pengguna TEXT,
        isi_pesan TEXT,
        tanggal_kirim TEXT,
        status TEXT,
        FOREIGN KEY (id_pengguna) REFERENCES PENGGUNA(id_pengguna)
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS TANGGAPAN (
        id_tanggapan TEXT PRIMARY KEY,
        id_pesan TEXT,
        id_pengguna TEXT,
        isi_tanggapan TEXT,
        tanggal_tanggapan TEXT,
        FOREIGN KEY (id_pesan) REFERENCES PESAN(id_pesan),
        FOREIGN KEY (id_pengguna) REFERENCES PENGGUNA(id_pengguna)
    );
    """)
    
    conn.commit()
    return conn
# ==========================================
# FITUR 1: EXPORT DATA KE JSON
# ==========================================
def export_data():
    conn = hit_database()
    cursor = conn.cursor()
    
    try:
        print("Memulai export data...")
        
        # 1. Ambil data Pengguna
        cursor.execute("SELECT id_pengguna, username, email, password FROM PENGGUNA")
        pengguna_rows = cursor.fetchall()
        list_pengguna = [
            {"id_pengguna": r[0], "username": r[1], "email": r[2], "password": r[3]} 
            for r in pengguna_rows
        ]
        
        # 2. Ambil data Pesan
        cursor.execute("SELECT id_pesan, id_pengguna, isi_pesan, tanggal_kirim, status FROM PESAN")
        pesan_rows = cursor.fetchall()
        list_pesan = [
            {"id_pesan": r[0], "id_pengguna": r[1], "isi_pesan": r[2], "tanggal_kirim": r[3], "status": r[4]} 
            for r in pesan_rows
        ]
        
        # 3. Ambil data Tanggapan
        cursor.execute("SELECT id_tanggapan, id_pesan, id_pengguna, isi_tanggapan, tanggal_tanggapan FROM TANGGAPAN")
        tanggapan_rows = cursor.fetchall()
        list_tanggapan = [
            {"id_tanggapan": r[0], "id_pesan": r[1], "id_pengguna": r[2], "isi_tanggapan": r[3], "tanggal_tanggapan": r[4]} 
            for r in tanggapan_rows
        ]
        
        # Gabungkan semua tabel ke satu objek dict
        data_gabungan = {
            "pengguna": list_pengguna,
            "pesan": list_pesan,
            "tanggapan": list_tanggapan
        }
        
        # Simpan menjadi file JSON
        with open('data_export.json', 'w', encoding='utf-8') as f:
            json.dump(data_gabungan, f, indent=4)
            
        print("✅ Export BERHASIL! File 'data_export.json' telah dibuat.")
        
    except Exception as e:
        print(f"❌ Export GAGAL: {e}")
    finally:
        conn.close()

# ==========================================
# FITUR 2: IMPORT DATA DARI JSON
# ==========================================
def import_data():
    if not os.path.exists('data_export.json'):
        print("❌ Gagal Import: File 'data_export.json' tidak ditemukan!")
        return

    conn = hit_database()
    cursor = conn.cursor()
    
    try:
        print("Memulai import data...")
        
        # Baca file JSON
        with open('data_export.json', 'r', encoding='utf-8') as f:
            data_import = json.load(f)
            
        # 1. Import PENGGUNA dulu (Urutan penting karena Foreign Key)
        if "pengguna" in data_import:
            for p in data_import["pengguna"]:
                cursor.execute("""
                    INSERT OR IGNORE INTO PENGGUNA (id_pengguna, username, email, password)
                    VALUES (?, ?, ?, ?)
                """, (p["id_pengguna"], p["username"], p["email"], p["password"]))
            print("-> Data Pengguna berhasil dimasukkan.")
            
        # 2. Import PESAN
        if "pesan" in data_import:
            for m in data_import["pesan"]:
                cursor.execute("""
                    INSERT OR IGNORE INTO PESAN (id_pesan, id_pengguna, isi_pesan, tanggal_kirim, status)
                    VALUES (?, ?, ?, ?, ?)
                """, (m["id_pesan"], m["id_pengguna"], m["isi_pesan"], m["tanggal_kirim"], m["status"]))
            print("-> Data Pesan berhasil dimasukkan.")
            
        # 3. Import TANGGAPAN
        if "tanggapan" in data_import:
            for t in data_import["tanggapan"]:
                cursor.execute("""
                    INSERT OR IGNORE INTO TANGGAPAN (id_tanggapan, id_pesan, id_pengguna, isi_tanggapan, tanggal_tanggapan)
                    VALUES (?, ?, ?, ?, ?)
                """, (t["id_tanggapan"], t["id_pesan"], t["id_pengguna"], t["isi_tanggapan"], t["tanggal_tanggapan"]))
            print("-> Data Tanggapan berhasil dimasukkan.")
            
        conn.commit()
        print("✅ Import BERHASIL! Data tersinkronisasi.")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ Import GAGAL: {e}")
    finally:
        conn.close()

# ==========================================
# CARA MENUNJUKKAN HASIL (Uji Coba)
# ==========================================

# Aktifkan salah satu dengan menghapus tanda pagar (#) untuk mengetes

# export_data()   # Jalankan ini untuk Export data database ke JSON
import_data()    # Jalankan ini untuk Import data JSON ke database
