import random
import time

print("**********************************************")
rastgele_sayi = random.randint(1,40)

tahmin_hakkı = 7
while True:
    tahmin = int(input("Tahmininiz"))
    if (tahmin< rastgele_sayi):
        print("Sorgulanıyor.....")
        time.sleep(1)
        print("Daha yüksek sayı söyleyin")
        tahmin_hakkı-=1
    elif(tahmin>rastgele_sayi):
        print("Sorgulanıyor.....")
        time.sleep(1)
        print("Daha düşük sayı söyleyin")
        tahmin_hakkı -= 1
    else:
        print("SRorgulanıyoe....")
        time.sleep(1)
        print("Tebrikler Sayınız",rastgele_sayi)
        break
    if(tahmin_hakkı == 0):
        print("tahmin hakknız bitti")
        print("Sayi = ",rastgele_sayi)





