from kirim_pesan import kirim_pesan
from moderasi import menu_moderasi
from respon import menu_respon
from aktivasi import hit_database 


hit_database()

while True:
    print("\n==========================")
    print("   FORUM PESAN ANONIM    ")
    print("==========================")
    print("1. 📝 Kirim Pesan")
    print("2. 👨‍💻 Moderasi Pesan")
    print("3. 💭 Tanggapan")
    print("4. 🚪 Keluar") 

    pilihan = input("Pilih menu : ")

    if pilihan == "1":
        kirim_pesan()
    elif pilihan == "2":
        
        password = input("Masukkan Password Admin: ")
        if password == "admin123":
            menu_moderasi()
        else:
            print("Password salah! Anda tidak memiliki akses.")
    elif pilihan == "3":
        menu_respon()
    elif pilihan == "4":
        print("Program selesai. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak tersedia.")