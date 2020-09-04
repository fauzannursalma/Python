# 00-Template
# Python -> Bahasa Pemrograman Interpreted
# Source Code (main.py) --> Interpreter (python) --> Terminal (di Run)
# Python Tidak perlu Complied
""" ini comment dalam multiline"""
# print("Hello World")
# print("Hello World")
# print("Hello World")
# a = 10
# b = 5
# print(a + b)

# Kita bisa meng-compile python menggunakan bytecode
# cara meng-compile
# Buka Terminal
# python -m py_compile main.py
# Kelebihannya Lebih cepat menjalankan program dibandingkan dengan Interprete

#==============================================================================================#


# 01-variabel
# Variabel adalah tempat menyimpan data
print("===========================")
print("01 - VARIABEL")
print("===========================")
print()
# Menaruh / assigment nilai (tanpa deklarasi cth : int a)
a = 10
x = 5
panjang = 1000

# Pemanggilan Pertama
print("Nilai a = ", a)
print("Nilai x = ", x)
print("Nilai Panjang = ", panjang)

# Penamaan
nilai_y = 15  # boleh menggunakan underscore
juta10 = 10000000  # boleh menggunakan numerik asal tidak diawal
nilaiZ = 17.5

# Pemanggilan Kedua
print("========================")
print("Nilai y = ", nilai_y)
print("Nilai z = ", nilaiZ)
print("Nilai juta10 = ", juta10)
nilai_y = 30
print("Nilai y = ", nilai_y)

# Assigment indirect
juta10 = nilaiZ
print("Nilai juta10 = ", juta10)
