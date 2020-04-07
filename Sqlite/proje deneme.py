from kütüphane import *
print("""
****************
Kütüphane programına hoşgeldiniz
İşlemler:
1. Kitapları Göster
2. Kitap Sorgulama
3. Kitap Ekle
4. Kitap Sil
5. Baskı Yükselt
Çıkmak için 'q' ya basınız

*******************
""")



kütüphane = Kütüphane()


while True:
    islem = input("Yapacağınız işlem")
    if(islem == "q"):
        print("Program sonlanıyor")
        break
    elif(islem == "1"):
        kütüphane.kitapları_goster()
    elif (islem == "2"):
        isim = input("Hangi kitabı istiyorsunuz")
        print("Kitap Sorgulanıyor")
        time.sleep(1)
        kütüphane.kitap_sorgula(isim)
    elif (islem == "3"):
        kitap_ekle = input("Eklenecek kitap nedir")
        yazar = input("Yazarı nedir ?")
        yayınevi = input("Yayınevi ?")
        tür = input("Tür ? ")
        baskı = int(input("Kaçıncı baskı"))
        yeni_kitap = Kitap(kitap_ekle,yazar,yayınevi,tür,baskı)
        time.sleep(1)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap Eklendi")
    elif (islem == "4"):
        kitap = input("Hangi kitabı silmek istiyorsunuz")
        cevap =  input("Emin misiniz E/H")
        if(cevap == "E"):
            print("Kitap siliniyor")
            time.sleep(1)
            kütüphane.kitap_sil(kitap)
            print("Kitap silindi")

    elif (islem == "5"):
        isim = input("Hangi kitabın baskısını yükselteceksiniz")
        print("Baskı Yükseltiliyor")
        time.sleep(1)
        kütüphane.baskı_yükselt(isim)
        print("Baskı Yükseltildi")
    else:
        print("Geçersiz işlem")





































