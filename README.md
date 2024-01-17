def tambah(a,b):
 return a + b
 print("pilihan operasi : ")
 print("1.penjumlahan")
 print("2.pengurangan")
 print("3.perkalian")

 pilihan = input("masukkan pilihan (1/2/3) : ")

 if pilihan in (1,2,3):
   angka1 = int(input("masukkan bilangan pertama : "))
   angka2 = int(input("masukkan bilangan kedua   : "))

   if pilihan == '1':
     print(angka1,"+",angka2,'=',tambah(angka1, angka2))
   else:
     print("pilihan tidak valid")
