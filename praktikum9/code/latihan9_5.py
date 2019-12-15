gandakan_angka = lambda n: (n * 2) # Mengandakan nilai n
pangkat_angka = lambda n: (n ** 2) # Mempangkatkan nilai n
cek_bilangan_genap = lambda n: n <= 5 # Mengecek n lebih besar sama dengan 5
hello = lambda: ("INDRIAN") # Fungsi ini Mengembalikan nilai nama INDRIAN

print("Hallo ", hello())
print(gandakan_angka(5))
print(cek_bilangan_genap(7))
print(pangkat_angka(32))

angka_ajaib = [1, 2, 3, 4, 5, 6, 7, 8]

print(list(map(lambda angka: (angka * 2), angka_ajaib)))    # Mengandakan nilai setiap element Set
print(list(map(lambda angka: (angka ** 2), angka_ajaib)))   # Mempangkatkan nilai setiap element Set
print(list(map(lambda angka: (angka <= 5), angka_ajaib)))   # Mengecek nilai setiap element Set 
                                                            # dengan lebih dari 5