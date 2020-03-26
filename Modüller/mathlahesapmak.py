import math
print("1-Faktoriyel"
      "2-Logaritma"
      "3-Karekök"
      "4-Karesi ")
islem =int(input("Hangi işlemi yapmak istiyorsunuz"))

sayi = int(input("Saayı giriniz"))
if(islem == 1):
   print(math.factorial(sayi))

elif(islem == 2):
 print(math.log10(sayi))
elif(islem == 3):
    print(math.sqrt(sayi))
elif(islem == 4):
   print( math.pow(sayi,2))
