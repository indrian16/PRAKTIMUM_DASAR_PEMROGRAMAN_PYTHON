nama = ["INDRIAN", "RIAN"]
nim = [19, 11, 10, 24, 41, 00, 3]
backup = nama.copy()

# Method append()
nama.append("INDRIAN S.kom")
print(nama)

# Method clear()
nama.clear()
print(nama)

# Method copy()
nama = backup.copy()
print(nama)

# Method count(<ELEMEN>)
print(nama.count("INDRIAN"))

# Method extend(<INTERABLE>)
nama.extend(nim)
print(nama)

# Method index(<ELEMEN>)
print(nama.index("RIAN"))
print(nim.index(3))

# Method insert(<POSISI>, <ELEMEN>)
nama.insert(2, "Indrian S.kom")
print(nama)

# Method pop([<INDEX>])
nama.pop(2)
print(nama)

# Method remove(<ELEMEN>)
nama.remove("RIAN")
print(nama)

# Method reverse()
nama.reverse()
print(nama)

# Method sort([OPTION])
backup.sort()
print(backup)
backup.sort(reverse=True)
print(backup)

def byLine(e):
    return len(e)
backup.sort(key=byLine)
print(backup)