name = {"INDRIAN", "RIAN", 1911102441003}
newName = {}
print(name, newName)

# Method add(<ELEMENT>)
name.add("Android Developer")

# Method copy()
newName = name.copy()
print(newName)

# Method clear()
newName.clear()
print(newName)

# Method difference(<SET>)
newName = newName.copy()
name.add("Flutter Developer")
print(name.difference(newName))

# Method discard(<ELEMEN>)
name.discard("Flutter Developer")
newName.clear()
newName.add("Android Developer")
print(name)

# Method intersection(<SET>)
print(name.intersection(newName))

# Method intersection_update ()
newName.intersection_update(name)
print(newName)

# Method isdisjoint()
print(name.isdisjoint(newName))

# Method issuperset(<SET>)
print(name.issuperset(newName))

# Method pop()
name.pop()
print(name)

# Method remove(<ELEMEN>)
name.remove("RIAN")
print(name)

# Method symmetric_difference(<SET>)
newName.symmetric_difference(name)
print(newName)

# Method symmetric_difference_update(<SET>)
name.symmetric_difference_update(newName)
print(name)

# Method union(<SET>)
name.union(newName)
print(name)

# Method update(<SET>)
name.update(newName)
print(name)