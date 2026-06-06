# Muhammad Abdi Rauf
# 1801623074
# Tugas 8 Looping For Statement

for baris in range(8):
    for kolom in range(8):
        if (baris + kolom) % 2 == 0:
            print("⬛", end="")
        else:
            print("⬜", end="")
    print()