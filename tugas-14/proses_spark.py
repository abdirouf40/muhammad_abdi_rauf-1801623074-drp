import json

print("\n=== Memulai Analisis Data Forum Curhat (Simulasi MapReduce) ===")

# 1. Membaca file json curhat yang sukses kamu buat sebelumnya
try:
    with open("forum_curhat_dummy.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("❌ File 'forum_curhat_dummy.json' tidak ditemukan!")
    exit()

# 2. KETENTUAN SOAL: Memecah data raya menjadi 2 bagian data (Simulasi 2 Node)
setengah_data = len(data) // 2
node_1 = data[:setengah_data]  # 20.000 data pertama masuk ke Node 1
node_2 = data[setengah_data:]  # 20.000 data sisa masuk ke Node 2

print(f"[INFO]: Data sukses dipecah menjadi 2 Bagian Mandiri (Node 1 & Node 2).")
print(f"[INFO]: Node 1 memproses {len(node_1)} data curhat.")
print(f"[INFO]: Node 2 memproses {len(node_2)} data curhat.\n")

# 3. PROSES MAPREDUCE: Setiap Node menghitung total views per kategori secara barengan
total_views_per_kategori = {}

# Node 1 mulai memetakan (Map) dan menjumlahkan
for item in node_1:
    kat = item["kategori"]
    total_views_per_kategori[kat] = total_views_per_kategori.get(kat, 0) + item["jumlah_views"]

# Node 2 mulai memetakan (Map) dan menjumlahkan hasilnya ke wadah yang sama (Reduce)
for item in node_2:
    kat = item["kategori"]
    total_views_per_kategori[kat] = total_views_per_kategori.get(kat, 0) + item["jumlah_views"]

# 4. TAMPILKAN HASILNYA DALAM BENTUK TABEL RAPI (Sama persis seperti .show() milik Spark)
print("=== TOTAL KUNJUNGAN (VIEWS) PER KATEGORI CURHAT ===")
print("-" * 50)
print(f"{'Kategori':<25} | {'Total Jumlah Views':<15}")
print("-" * 50)
for kategori, total_views in total_views_per_kategori.items():
    print(f"{kategori:<25} | {total_views:<15,}")
print("-" * 50)