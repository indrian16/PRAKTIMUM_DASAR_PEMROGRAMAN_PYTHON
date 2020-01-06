import worker as w

budi = w.Worker("Budi", 1000)
setiawan = w.Worker("Setiawan", 1000)
workers = [
    budi,
    setiawan
]

budi.printPekerja()
setiawan.printPekerja()
print("Object Size: ", len(workers))


totalSalary = 0
for s in workers:
    totalSalary += s.salary

print("Total salary: $", totalSalary)

