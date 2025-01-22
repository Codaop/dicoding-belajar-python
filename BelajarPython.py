import random

# trunk-ignore-all(ruff/E999)
# contoh slicing string
y = ["ayam", "bebek", "tempe", "hati", "otak", "perkedel", "makan"]
print(y[0:5:2])

x = "Makan enak"
print(x[2:])

# contoh formatted string
name = "Perseus Evans"
print(f"Hello, nama saya {name}")

# contoh %-formatting
name = "Perseus Evans"
print("Hello, nama saya %s" % name)

# contoh str.format()
name = "Evangelion"
umur = 19
print("Nama saya {}, umur saya {}".format(name, umur))

# contoh tipe data list
var_list = ["Makan", 20, 0.9, "Hahaha"]
print(type(var_list))
print(var_list[2])

# contoh tipe data set
set1 = {1, 2, 4, 5, 7, 8}
set2 = {1, 9, 8, 7, 5, 6}

union = set1.union(set2)
print(f"Union: {union}")

intersection = set2.intersection(set1)
print("Intersection: ", intersection)

# contoh dictionary
varX = {"nama": "Ryan", "umur": 19, "hobi": "Fotografi"}
varX["Kelas"] = "XII MIA 1"

print("Data Siswa:")
print("Nama Siswa =", varX["nama"])
print("Umur =", varX["umur"])
print("Hobi =", varX["hobi"])
print("Kelas =", varX["Kelas"])

# contoh memanggil elemen dalam set
# iterasi
set1 = {1, 2, 3, 4, 5}
for elemen in set1:
    print(elemen)

    # metode pop elemen
set1 = {1, 2, 3, 4, 5}
print(set1.pop())

# metode pop elemen
set1 = {1, 2, 3, 4, 5}
random_set1 = random.choice(list(set1))  # import random
print(random_set1)

# mengubah ke bentuk list
set1 = {1, 2, 3, 4, 5}
list_set1 = list(set1)
print(list_set1[2])
