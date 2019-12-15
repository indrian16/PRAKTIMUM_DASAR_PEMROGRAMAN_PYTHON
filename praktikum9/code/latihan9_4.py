def recursive(num): # Definisi fungsi recursive dengan param num
    if num > -5: # Mengecek kondisi num lebih besar dari -5
        print(num) # Print num sesuai dari paramter
        num = num - 1 # Menurangi nilai num -1
        recursive(num) # Memangil fungsi dirinya sendiri
    else: # kondisi num kurang dari -5
        print(num) # Print num sesuai dari paramter

in_num = int(input("Masukan angka pertama: ")) # Input angka pertama
in_num2 = int(input("Masukan angka kedua: ")) # Input angka kedua
recursive(in_num) # Memangil fungsi recursive
recursive(in_num2) # Memangil fungsi recursive