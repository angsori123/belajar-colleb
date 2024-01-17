def tambah(angka1, angka2):
  return bil_a + bil_b
def kurang(bil a, bil b):
  return bil_a - bil_b
def lali (a, b):
  return a x b

print("pilih oprasi : ")
print("1. penjumlahan : ")
print("2. pengurangan : ")
print("3. perkalian : ")

pilih = input("masukan pilihan (1/2/3) : ")

if pilihan in ('1', '2', '3'):
  angka1 = int(input("masukan bilangan pertama : "))
  angka2 = int(input("masukan bilangan kedua : "))

if pilihan == '1':
  print(angka1. "+", angka2, "=", tambah(angka1, angka2))
else:
  print("pilihan tidak valid")

if pilihan == '2':
  print(angka1. "-", angka2, "=", kurang(angka1, angka2))
