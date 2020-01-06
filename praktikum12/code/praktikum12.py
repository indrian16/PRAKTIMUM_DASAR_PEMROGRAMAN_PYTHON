f_bio = open("F:\\UMKT\\PRAKTIKUM\\PRAKTIMUM_DASAR_PEMROGRAMAN_PYTHON\\praktikum12\\code\\bio.txt", "r")

bio = f_bio.read()
print(bio)
f_bio.close()
del f_bio

f_bio = open("F:\\UMKT\\PRAKTIKUM\\PRAKTIMUM_DASAR_PEMROGRAMAN_PYTHON\\praktikum12\\code\\sosial_media.txt", "w")
github = str("https://github.com/"+input("Input your github: "))
medium = str("https://medium.com/"+input("Input your Medium: "))
stackoverflow = str("https://stackoverflow.com/"+input("Input your stackoverflow: "))
in_texts = [
    github,
    medium,
    stackoverflow
]
texts = ""
for i in in_texts:
    
    texts += i+"\n"

f_bio.write(texts)
f_bio.close()
