bio = {
    "name": "INDRIAN",
    "nim": 1911102441003
}
backup_bio = bio.copy()
print(bio)


# Method clear()
bio.clear()
print(bio)

# Method copy()
bio = backup_bio.copy()
print(bio)

# Method formkeys(<KEY>[, <VALUES>])
x = {"key1", "key2", "key3"}
print(dict.fromkeys(x, 16))

# Method get(<INDEX>)
print(bio.get("nim"))

# Method items()
print(bio.items())

# Method keys()
print(bio.keys())

# Method pop()
bio.pop("name")
print(bio)

# Method setdefault()
x = bio.setdefault("prodi", "Teknik Informatika")
print(x)

# Method update()
bio.update({"name": "INDRIAN"})
print(bio)

# Method values()
print(bio.values())