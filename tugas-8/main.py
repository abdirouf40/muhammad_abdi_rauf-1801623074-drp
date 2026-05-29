#Program Catur & Manajemen Aktivitas

def cetak_papan_catur():
    """
    Mencetak papan catur 8x8 menggunakan for statement.
    Hitam: ⬛ 
    Putih: ⬜ 
    """
    hitam = '⬛'
    putih = '⬜'
    print("\n" + "=" * 30)
    print("        PAPAN CATUR")
    print("=" * 30)
    for baris in range(8):
        for kolom in range(8):
            if (baris + kolom) % 2 == 0:
                print(hitam, end="  ")
            else:
                print(putih, end="  ")
        print()
    print("=" * 30)
    print("Keterangan: ⬛ = Hitam, ⬜ = Putih\n")

def main():
    cetak_papan_catur()
    daftar_aktivitas = []
    print("=== INPUT AKTIVITAS ===")
    print("Masukkan aktivitas satu per satu. Ketik 'selesai' untuk mengakhiri input.\n")
    while True:
        aktivitas = input("Aktivitas: ").strip()
        if aktivitas.lower() == 'selesai':
            break
        if aktivitas == "":
            print("Aktivitas tidak boleh kosong. Silakan ulangi.")
            continue
        daftar_aktivitas.append({"aktivitas": aktivitas, "info": ""})
        print(f"✓ '{aktivitas}' berhasil ditambahkan.\n")
    print("\n" + "=" * 50)
    print("DAFTAR AKTIVITAS (SAAT INI)")
    print("=" * 50)
    if not daftar_aktivitas:
        print("Belum ada aktivitas yang dimasukkan.")
    else:
        for i, item in enumerate(daftar_aktivitas, start=1):
            print(f"{i}. {item['aktivitas']}")
    print("=" * 50)
    if daftar_aktivitas:
        print("\n=== TAMBAH INFORMASI TAMBAHAN ===")
        print("Anda dapat menambahkan keterangan seperti waktu, tempat, prioritas, dll.\n")
        while True:
            try:
                pilihan = input(f"Pilih nomor aktivitas (1-{len(daftar_aktivitas)}) untuk ditambahi info, atau 0 untuk selesai: ")
                if pilihan == '0':
                    break
                idx = int(pilihan) - 1
                if 0 <= idx < len(daftar_aktivitas):
                    info_baru = input(f"Masukkan info untuk '{daftar_aktivitas[idx]['aktivitas']}': ").strip()
                    if info_baru:
                        daftar_aktivitas[idx]['info'] = info_baru
                        print("✓ Informasi berhasil ditambahkan.\n")
                    else:
                        print("Info tidak boleh kosong. Silakan ulangi.\n")
                else:
                    print(f"Nomor harus antara 1 dan {len(daftar_aktivitas)}.\n")
            except ValueError:
                print("Masukkan angka yang valid.\n")
    print("\n" + "=" * 50)
    print("DAFTAR AKTIVITAS LENGKAP (DENGAN INFO)")
    print("=" * 50)
    if not daftar_aktivitas:
        print("Tidak ada aktivitas untuk ditampilkan.")
    else:
        for i, item in enumerate(daftar_aktivitas, start=1):
            if item['info']:
                print(f"{i}. {item['aktivitas']} → 📝 {item['info']}")
            else:
                print(f"{i}. {item['aktivitas']} → (belum ada info tambahan)")
    print("=" * 50)
    print("\nTerima kasih telah menggunakan program ini!")

if __name__ == "__main__":
    main()