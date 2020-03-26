girilen_sayi = int(input("Lütfen bir sayı giriniz"))
i = 1
toplam = 0
while(i<girilen_sayi):
    if(girilen_sayi%i == 0):
        toplam+=i
    i+=1
if(toplam == girilen_sayi):
    print("Mükemmel sayıdır")
else:
    print("Mükemmel sayı değildir")