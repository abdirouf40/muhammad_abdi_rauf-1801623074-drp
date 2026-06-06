# database.py
list_pesan_pending = []  # Antrean pesan baru untuk admin
list_pesan_publik = []   # Pesan yang lolos moderasi dan tampil di forum
# display.py
def tampilkan_menu_utama():
    print("\n" + "="*35)
    print("    FORUM BERBAGI PESAN ANONIM     ")
    print("="*35)
    print(" 1. Kirim Pesan Anonim (User)")
    print(" 2. Menu Moderasi (Admin)")
    print(" 3. Lihat Forum & Beri Respon (Umum)")
    print(" 4. Keluar")
    print("="*35)

def tampilkan_pesan_forum(list_pesan):
    if not list_pesan:
        print("\n[i] Forum masih kosong.")
        return
        
    print("\n--- LINIMASA FORUM ANONIM ---")
    for idx, item in enumerate(list_pesan, 1):
        print(f"\n[{idx}] Pengguna Anonim: \"{item['isi_pesan']}\"")
        
        # Tambahan: Menampilkan komentar jika ada yang menanggapi
        if item['komentar']:
            print("    Tanggapan:")
            for komen in item['komentar']:
                print(f"    -> {komen}")
