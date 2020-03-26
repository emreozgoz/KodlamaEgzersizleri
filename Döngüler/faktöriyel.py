sayi = int(input("Hangi sayının faktöriyelini alırsınız"))
print(*range(1,sayi+1))

while True:
    if(sayi == "q"):
        print("Programdan Sonlandırılıyor")
        break
    else:
        faktoriyel = 1
        for i in range(2,sayi+1):
            faktoriyel *= i
            print(faktoriyel)
    break


