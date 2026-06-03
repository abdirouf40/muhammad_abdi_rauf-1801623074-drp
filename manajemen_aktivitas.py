from datetime import datetime


def tampilkan_header():
    print("=" * 50)
    print("   APLIKASI MANAJEMEN AKTIVITAS HARIAN")
    print("=" * 50)


def aktivitas_sarapan():
    print("\n AKTIVITAS: SARAPAN")
    print("Bahan makanan yang tersedia di lokasi Anda:")
    print("  1. Telur")
    print("  2. Ikan")
    print("  3. Nugget")
 

    menu = input("Masukkan menu sarapan yang Anda inginkan: ").strip().lower()

    bahan_tersedia = ["telur", "ikan", "nugget"]

    if menu in bahan_tersedia:
        print(f"   Bahan '{menu.capitalize()}' tersedia di lokasi Anda.")
        print(f"   Silakan masak '{menu.capitalize()}' terlebih dahulu sebelum sarapan.")
    else:
        print(f"   Bahan TIDAK tersedia di lokasi Anda.")
        print(f"   Anda perlu membeli bahan terlebih dahulu.")


def aktivitas_berangkat_kerja():
    print("\n AKTIVITAS: BERANGKAT KERJA")

    JAM_MASUK_KERJA = 8  # Jam 08:00

    waktu_sekarang = datetime.now()
    jam_sekarang = waktu_sekarang.hour
    menit_sekarang = waktu_sekarang.minute

    print(f"Jadwal masuk kerja  : 08:00")
    print(f"Waktu saat ini      : {waktu_sekarang.strftime('%H:%M:%S')} ({waktu_sekarang.strftime('%A, %d %B %Y')})")

    if jam_sekarang < JAM_MASUK_KERJA:
        sisa_menit = (JAM_MASUK_KERJA - jam_sekarang) * 60 - menit_sekarang
        sisa_jam = sisa_menit // 60
        sisa_mnt = sisa_menit % 60
        print(f"   Anda BELUM terlambat masuk kerja.")
        if sisa_jam > 0:
            print(f"   Sisa waktu sebelum jam masuk: {sisa_jam} jam {sisa_mnt} menit.")
        else:
            print(f"   Sisa waktu sebelum jam masuk: {sisa_mnt} menit.")
        print(f"   Segera bersiap dan berangkat agar tidak terlambat!")

    elif jam_sekarang == JAM_MASUK_KERJA and menit_sekarang == 0:
        print(f"   Tepat waktu! Sekarang tepat jam 08:00.")
        print(f"   Segera berangkat agar tidak terlambat!")

    else:
        if jam_sekarang == JAM_MASUK_KERJA:
            terlambat_menit = menit_sekarang
        else:
            terlambat_menit = (jam_sekarang - JAM_MASUK_KERJA) * 60 + menit_sekarang

        terlambat_jam = terlambat_menit // 60
        terlambat_mnt = terlambat_menit % 60

        print(f"   Anda SUDAH TERLAMBAT masuk kerja!")
        if terlambat_jam > 0:
            print(f"   Keterlambatan: {terlambat_jam} jam {terlambat_mnt} menit.")
        else:
            print(f"   Keterlambatan: {terlambat_mnt} menit.")
        print(f"   Segera hubungi atasan atau pimpinan Anda.")

def main():
    tampilkan_header()
    print("\nDaftar aktivitas yang tersedia:")
    print("  1. Sarapan")
    print("  2. Berangkat Kerja")
    print("  3. Keluar")
    print("-" * 50)

    while True:
        aktivitas = input("\nMasukkan aktivitas yang akan Anda lakukan: ").strip().lower()

        if aktivitas in ["sarapan", "1"]:
            aktivitas_sarapan()
        elif aktivitas in ["berangkat kerja", "berangkat", "kerja", "2"]:
            aktivitas_berangkat_kerja()
        elif aktivitas in ["keluar", "exit", "quit", "3"]:
            print("\n Terima kasih telah menggunakan Aplikasi Manajemen Aktivitas!")
            print("   Semoga hari Anda menyenangkan!\n")
            break
        else:
            print(f"\n  Aktivitas tidak dikenali.")
            print("   Silakan masukkan: 'sarapan', 'berangkat kerja', atau 'keluar'.")

        print("\n" + "=" * 50)
        lanjut = input("Apakah Anda ingin memasukkan aktivitas lain? (ya/tidak): ").strip().lower()
        if lanjut not in ["ya", "y"]:
            print("\n Terima kasih telah menggunakan Aplikasi Manajemen Aktivitas!")
            print("   Semoga hari Anda menyenangkan!\n")
            break


if __name__ == "__main__":
    main()
