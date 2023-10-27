# ganjil genap
for i in range(10):
    if i % 2 == 1:
        print(i)
    elif i % 2 == 0:
        print(i)

#logika penilaian
nilai_angka = 101

if 0<= nilai_angka <= 100:
     if nilai_angka > 80:
        print("nilai angka:", nilai_angka,"nilai hufuf: A")
     elif 70< nilai_angka <= 80:
        print("nilai angka:", nilai_angka,"nilai hufuf: AB")
elif 0< nilai_angka<=70:
 print("E")

else:
   print("bzier")


  #how ATM works

pin = input("Masukan PIN Anda:")
saldo = 100000

if pin == "14082013":
    print("* MENU ATM***")
    print("1. Tampilkan saldo")
    print("2. Tarik uang")
    pilihan = input("pilih :")
    
    #print("anda memilih:",pilihan)
    if pilihan == "1":
        print("saldo anda :", saldo)
    elif pilihan =="2" :
        jml_tarik = int(input("Masukan jml uang yang akan ditarik"))
        print("anda akan mengambil :",jml_tarik)
        saldo = saldo - jml_tarik
        print("saldo akhir anda :",saldo)
        
    else:
        print("MILIH CAWAPRES BRO?!!")
        
    
else:
    print("Pin anda salah!")
    
     
