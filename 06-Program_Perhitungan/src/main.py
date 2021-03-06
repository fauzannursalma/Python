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

# // Tipe Data Standar
# Tipe Data : Angka satuan yang ngga ada koma-nya (integer)
# from ctypes import c_double
# data_integer = 11
# print(data_integer, " = Tipe Data ", type(data_integer))

# # Tipe Data : Angka Pecahan/ koma (float)
# data_float = 9.5
# print(data_float, " = Tipe Data ", type(data_float))

# # Tipe Data : Kumpulan Karakter (string)
# data_string = "Fauzan"
# print(data_string, " = Tipe Data ", type(data_string))

# # Tipe Data :  Biner true/false (boolean)
# data_boolean = True
# print(data_boolean, " = Tipe Data ", type(data_boolean))
# print()

# # // Tipe Data Khusus
# # Tipe Data : Bilangan Kompleks contoh : 10 + 5i
# data_complex = complex(5, 6)  # if > j = imaginer
# print(data_complex, " = Tipe Data ", type(data_complex))

# # Tipe Data : dari Bahasa C
# data_cDouble = c_double(11.5)
# print(data_cDouble, " = Tipe Data ", type(data_cDouble))

#==============================================================================================#

# 03- CASTING TIPE DATA /////
# Merubah dari suatu tipe data ke tipe data lain
# Tipe Data = int, float, string, boolean
# print("===========================")
# print("03 - CASTING TIPE DATA")
# print("===========================")
# print()
# # integer
# print("-----> integer <-----")
# data_int = 9
# print(data_int, " = Tipe Data ", type(data_int))
# data_float = float(data_int)
# data_string = str(data_int)
# data_boolean = bool(data_int)  # akan False jika nilai = 0
# print(data_float, " = Tipe Data ", type(data_float))
# print(data_string, " = Tipe Data ", type(data_string))
# print(data_boolean, " = Tipe Data ", type(data_boolean))
# print()

# # float
# print("-----> float <-----")
# data_float = 9.9
# print(data_float, " = Tipe Data ", type(data_float))
# data_int = int(data_float)  # dibulatkan ke bawah
# data_string = str(data_float)
# data_boolean = bool(data_float)  # akan False jika nilai = 0
# print(data_int, " = Tipe Data ", type(data_int))
# print(data_string, " = Tipe Data ", type(data_string))
# print(data_boolean, " = Tipe Data ", type(data_boolean))
# print()

# # boolean
# print("-----> boolean <-----")
# data_boolean = True  # True / False
# print(data_boolean, " = Tipe Data ", type(data_boolean))
# data_int = int(data_boolean)  # dibulatkan ke bawah
# data_string = str(data_boolean)
# data_float = float(data_boolean)  # akan False jika nilai = 0
# print(data_int, " = Tipe Data ", type(data_int))
# print(data_string, " = Tipe Data ", type(data_string))
# print(data_float, " = Tipe Data ", type(data_float))
# print()

# # string
# print("-----> string <-----")
# data_string = "10"
# print(data_string, " = Tipe Data ", type(data_string))
# data_int = int(data_string)  # String Harus Angka / Nomor
# data_float = float(data_string)  # String Harus Angka / Nomor
# data_boolean = bool(data_string)  # False jika string kosong
# print(data_int, " = Tipe Data ", type(data_int))
# print(data_float, " = Tipe Data ", type(data_float))
# print(data_boolean, " = Tipe Data ", type(data_boolean))

#==============================================================================================#

# 04 - MENGAMBIL INPUT DATA USER /////
# print("================================")
# print("04 - MENGAMBIL INPUT DATA USER")
# print("================================")
# print()

# # Data yang di Input pasti String
# data = input("Masukan Data [String] : ")
# print(data, " = Tipe Data ", type(data))

# # Jika ingin menginput integer [int]
# data_int = int(input("Masukan Data [Integer] : "))
# print(data_int, " = Tipe Data ", type(data_int))

# # Jika ingin menginput FLoat
# data_float = float(input("Masukan Data [Float] : "))
# print(data_float, " = Tipe Data ", type(data_float))

# # jika ingin menginput boolean
# data_biner = bool(int(input("Masukan Data [Boolean] : ")))
# print(data_biner, " = Tipe Data ", type(data_biner))

#==============================================================================================#

# # 05 - OPERASI ARITMATIKA /////
# print("================================")
# print("05 - OPERASI ARITMATIKA")
# print("================================")
# print()

# a = 5
# b = 2
# # Operasi Penjumlahan +
# print("-----> Penjumlahan <-----")
# hasil = a + b
# print(a, "+", b, " = ", hasil)

# # Operasi Pengurangan -
# print("-----> Pengurangan <-----")
# hasil = a - b
# print(a, "-", b, " = ", hasil)

# # Operasi Penjumlahan .
# print("-----> Perkalian <-----")
# hasil = a * b
# print(a, "x", b, " = ", hasil)

# # Operasi Penjumlahan /
# print("-----> Pembagian <-----")
# hasil = a / b
# print(a, "/", b, " = ", hasil)

# # Operasi Eksponen (pangkat) **
# print("-----> Eksponen / Pangkat <-----")
# hasil = a ** b
# print(a, "**", b, " = ", hasil)

# # Operasi Modulus %
# print("-----> Modulus <-----")
# hasil = a % b
# print(a, "%", b, " = ", hasil)

# # Operasi Floor division [Kebalikan Modulus]//
# print("-----> Floor division <-----")
# hasil = a // b
# print(a, "//", b, " = ", hasil)

# # Prioritas Operasi / Operational Precedence
# # 1) () (Tanda Kurung)
# # 2) **  (Eksponen / pangkat)
# # 3) * / % // (Perkalian, Pembagian, Modulus, Floor Division)
# # 4) + - (Penjumlahan & Pengurangan)

# print("-----> Contoh Priotitas Operasi<-----")
# hasil = (a + b) ** b
# print("(", a, " + ", b, ") **", b, " = ", hasil)

#==============================================================================================#

# 06 - Perhitungan Sederhana /////
print("================================")
print("06 - PROGRAM KONVERSI TEMPERATUR")
print("================================")
print()

# Celcius
celcius = float(input("Masukan Suhu (Celcius) : "))
print("Suhu adalah ", celcius, "Celcius")

# Reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur = ", reamur, "reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit = ", fahrenheit, "fahrenheit")

# Kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin = ", kelvin, "kelvin")
