def not_hesapla(satir):
    print(satir)

with open("dosya.txt","r",encoding="utf-8")as file:
    for i in file:
        not_hesapla(i)