height = float(input("Berapa tinggi badan anda? "))

if height < 154:
    print("Terlalu pendek")
elif height >= 154 and height <= 165:
    print("Cukup ideal")
elif height >= 166 and height <= 170:
    print("Ideal")
elif height >= 171 and height <= 176:
    print("Cukup tinggi")
else:
    print("Abnormal/Berlebih")
