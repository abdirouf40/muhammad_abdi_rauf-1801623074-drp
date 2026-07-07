from kirim_pesan import kirim_pesan
from moderasi import menu_moderasi
from respon import menu_respon
from export_json import export_json
from import_json import import_json

while True:

    print("\n==========================")
    print(" FORUM PESAN ANONIM ")
    print("==========================")
    print("1. Kirim Pesan")
    print("2. Moderasi Pesan")
    print("3. Tanggapan")
    print("4. Export JSON")
    print("5. Import JSON")
    print("6. Keluar")

    pilihan = input("Pilih menu : ")

    if pilihan == "1":
        kirim_pesan()

    elif pilihan == "2":
        menu_moderasi()

    elif pilihan == "3":
        menu_respon()

    elif pilihan == "4":
        export_json()

    elif pilihan == "5":
        import_json()

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")