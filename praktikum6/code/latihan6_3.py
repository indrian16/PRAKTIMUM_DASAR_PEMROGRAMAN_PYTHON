nama = ["INDRYAN", "RIAN"]
nim = [19, 11, 10, 24, 41, 00, 3]
matakuliah = ["pemograman", "dasar", "Android", "Flutter", "Java", "Kotlin", "Dart"]

print("==========Original not manipulation==========")
print(nama)
print(nim)
print(matakuliah)
print("=============================================")

# Merubah Elemen
nama[0] = "INDRIAN"
print(nama)

# Menghapus Elemen
del matakuliah[3]
del matakuliah[5]
print(matakuliah)

# Mengecek Elemen List
in_name = input("Sebutkan nama yang bikin program ini: ").upper()
if in_name in nama:
    print("Ya benar: ", in_name, "nama dia")
else:
    print("Salah coba lagi tulis yang benar")

# Perulangan pada List
i = 1
for study in matakuliah:
    print("[",i,"]", "Matakuliah: ", study)
    i+=1