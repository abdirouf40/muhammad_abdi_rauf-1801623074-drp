from datetime import datetime
from penyimpanan import muat_data, simpan_data, id_baru
 
 
def tampilkan_menu():
    print("\n=== FORUM PESAN ANONIM (Respon) ===")
    print("1. Lihat semua pesan & respon")
    print("2. Beri respon ke sebuah pesan")
    print("3. Edit respon")
    print("4. Hapus respon")
    print("5. Keluar")
 
 
def lihat_pesan(data):
    """READ: menampilkan semua pesan beserta respon-respon di bawahnya."""
    if not data:
        print("Belum ada pesan di forum.")
        return
 
    print("\n--- DAFTAR PESAN ---")
    for pesan in data:
        print(f"\n[id {pesan['id']}] ({pesan['waktu']})")
        print(f"  {pesan['isi']}")
 
        if pesan["respon"]:
            for r in pesan["respon"]:
                print(f"    -> respon id {r['id']}: {r['isi']}")
        else:
            print("    (belum ada respon)")
 
 
def cari_pesan(data, id_pesan):
    """Fungsi bantu: mencari objek pesan berdasarkan id-nya."""
    for pesan in data:
        if pesan["id"] == id_pesan:
            return pesan
    return None
 
 
def buat_respon(data):
    """CREATE: menambahkan respon baru ke sebuah pesan."""
    lihat_pesan(data)
    if not data:
        return
 
    try:
        id_pesan = int(input("\nMasukkan id pesan yang mau direspon: "))
    except ValueError:
        print("Id harus berupa angka.")
        return
 
    pesan = cari_pesan(data, id_pesan)
    if pesan is None:
        print("Id pesan tidak ditemukan.")
        return
 
    isi = input("Tulis respon anonim kamu: ").strip()
    if not isi:
        print("Respon tidak boleh kosong.")
        return
 
    respon_baru = {
        "id": id_baru(pesan["respon"]),
        "isi": isi,
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    pesan["respon"].append(respon_baru)
    simpan_data(data)
    print(f"Respon terkirim! (id respon: {respon_baru['id']})")
 
 
def edit_respon(data):
    """UPDATE: mengubah isi respon berdasarkan id pesan + id respon."""
    lihat_pesan(data)
    if not data:
        return
 
    try:
        id_pesan = int(input("\nMasukkan id pesan: "))
        id_respon = int(input("Masukkan id respon yang mau diedit: "))
    except ValueError:
        print("Id harus berupa angka.")
        return
 
    pesan = cari_pesan(data, id_pesan)
    if pesan is None:
        print("Id pesan tidak ditemukan.")
        return
 
    for r in pesan["respon"]:
        if r["id"] == id_respon:
            isi_baru = input(f"Isi sekarang: {r['isi']}\nIsi baru: ").strip()
            if isi_baru:
                r["isi"] = isi_baru
                simpan_data(data)
                print("Respon berhasil diperbarui.")
            else:
                print("Isi baru tidak boleh kosong, dibatalkan.")
            return
 
    print("Id respon tidak ditemukan.")
 
 
def hapus_respon(data):
    """DELETE: menghapus respon berdasarkan id pesan + id respon."""
    lihat_pesan(data)
    if not data:
        return
 
    try:
        id_pesan = int(input("\nMasukkan id pesan: "))
        id_respon = int(input("Masukkan id respon yang mau dihapus: "))
    except ValueError:
        print("Id harus berupa angka.")
        return
 
    pesan = cari_pesan(data, id_pesan)
    if pesan is None:
        print("Id pesan tidak ditemukan.")
        return
 
    for r in pesan["respon"]:
        if r["id"] == id_respon:
            konfirmasi = input(f"Yakin hapus respon id {id_respon}? (y/n): ").lower()
            if konfirmasi == "y":
                pesan["respon"].remove(r)
                simpan_data(data)
                print("Respon berhasil dihapus.")
            else:
                print("Dibatalkan.")
            return
 
    print("Id respon tidak ditemukan.")
 
 
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