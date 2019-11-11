grade = int(input("Kelas berapa anda sekarang? "))
t_out = "Anda masih "

if grade <= 6:
    print(t_out+"SD")
elif grade >= 7 and grade <= 9:
    print(t_out+"SMP")
elif grade >= 10 and grade <= 12:
    print(t_out+"SMA/SMK")
elif grade >= 13:
    print("Anda sudah lulus sekolah")

print("Terima Kasih")
