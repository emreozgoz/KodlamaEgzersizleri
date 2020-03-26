toplam = 0
while True:
    sayi = input("Sayı giriniz")

    if (sayi == "q"):
        print("PRogramdan çıkılıyor")
        break
    else:
        sayi = int(sayi)
        toplam += sayi
print(toplam)
