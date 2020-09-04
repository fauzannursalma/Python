# 00-TEMPLATE /////
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

# 01-VARIABEL /////
# Variabel adalah tempat menyimpan data

# Menaruh / assigment nilai (tanpa deklarasi cth : int a)
# a = 10
# x = 5
# panjang = 1000

# # Pemanggilan Pertama
# print("Nilai a = ", a)
# print("Nilai x = ", x)
# print("Nilai Panjang = ", panjang)

# # Penamaan
# nilai_y = 15  # boleh menggunakan underscore
# juta10 = 10000000  # boleh menggunakan numerik asal tidak diawal
# nilaiZ = 17.5

# # Pemanggilan Kedua
# print("========================")
# print("Nilai y = ", nilai_y)
# print("Nilai z = ", nilaiZ)
# print("Nilai juta10 = ", juta10)
# nilai_y = 30
# print("Nilai y = ", nilai_y)

# # Assigment indirect
# juta10 = nilaiZ
# print("Nilai juta10 = ", juta10)

#==============================================================================================#

# 02-TIPE DATA /////
from ctypes import c_double
print("===========================")
print("02 - TIPE DATA")
print("===========================")
print()

print("-----> Tipe Data Standar <-----")
# // Tipe Data Standar
# Tipe Data : Angka satuan yang ngga ada koma-nya (integer)
data_integer = 11
print(data_integer, " = Tipe Data ", type(data_integer))

# Tipe Data : Angka Pecahan/ koma (float)
data_float = 9.5
print(data_float, " = Tipe Data ", type(data_float))

# Tipe Data : Kumpulan Karakter (string)
data_string = "Fauzan"
print(data_string, " = Tipe Data ", type(data_string))

# Tipe Data :  Biner true/false (boolean)
data_boolean = True
print(data_boolean, " = Tipe Data ", type(data_boolean))
print()

print("-----> Tipe Data Khusus <-----")
# // Tipe Data Khusus
# Tipe Data : Bilangan Kompleks contoh : 10 + 5i
data_complex = complex(5, 6)  # if > j = imaginer
print(data_complex, " = Tipe Data ", type(data_complex))

# Tipe Data : dari Bahasa C
data_cDouble = c_double(11.5)
print(data_cDouble, " = Tipe Data ", type(data_cDouble))
