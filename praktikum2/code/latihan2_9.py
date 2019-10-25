name = "INDRIAN" # Variable ini bertipekan String yang berisikan nama saya
date = 16 # Variable ini bertipekan Int yang berisikan tanggal lahir saya

# Mengunakan Operator Aritmatika
print(date - 12) # date bernilai 16 dikurang dengan 12, maka hasilnya 4

# Mengunakan Operator Assignment
date += 16
print(date) # date bernilai 16 ditambah sama dengan 4, hasilnya 32

# Mengunakan Operator Perbandingan
print(name != date) # name berisi INDRIAN dan tidak masa dengan date = 16.

# Mengunakan Operator Logika
logic = not 16 < 4 # 4 lebih besar dari pada 16 adalah salah maka nilainya FALSE
print(logic)       # dengan operator not maka nilainya berubah sebaliknya 

# Mengunakan Operator Identitas
print(name is not "INDRYAN") # INDRYAN tidak sama dengan INDRIAN maka dia true

# Mengunakan Operator Keangotaan
print("R" in name)  # Pada sequence "R" terdapat nilai spesifik dengan INDRIAN
                    # Maka hasilnya TRUE
                    
# Mengunakan Operator Bitwese
print(date | 4) # date bernilai 32(100000) digankan dengan 4(100)
                # Mengunakan operator | (or) maka hasilnya 100100(36)
