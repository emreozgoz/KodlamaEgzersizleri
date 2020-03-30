import random
import time
class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses =1,kanal_listesi = ["TRT"],kanal = "TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    def tv_ac(self):
        if(self.tv_durum == "Açık"):
            print("TV zaten açık")
        else:
            print("Tv açılıyor")
            self.tv_durum = "Açık"
    def tv_kapat(self):
        if (self.tv_durum == "Kapalı"):
            print("Tv zatne kapalı")
        else:
            print("Tv kapanıyor")
            self.tv_durum == "Kapalı"
    def ses_ayarı(self):
        while True:
            cevap = input("Sesi azalt :<\n Sesi arttır >\n Çıkış: exit")
            if(cevap == "<"):
                if(self.tv_ses != 0):
                    self.tv_ses -=1
                    print("Ses",self.tv_ses)
            elif(cevap == ">"):
                if (self.tv_ses != 31):
                    self.tv_ses +=1
                    print("Ses",self.tv_ses)
            else:
                print("Ses Güncellendi",self.tv_ses)
                break
    def kanal_ekle(self,kanal_adı):
        print("Kanal Ekleniyor")
        time.sleep(1)
        self.kanal_listesi.append(kanal_adı)
        print("Kanal Eklendi")
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi) -1)
        self.kanal = self.kanal_listesi(rastgele)
        print("Şu anki kanal",self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "TV Durumu{}\n TV SES {}\n Kanal Listesi{}\nŞu ankı kanal{}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
kumanda = Kumanda()
print("""
Televizyon uygulaması

1. TV AÇ
2. TV KAPAT
3.SES AYARLARI
4.KANAL EKLE
5.KANAL SAYISI
6.RASTGELE KANALA GEÇME
7.TV BİLGİLERİ

ÇIKMAK İÇİN q YA BASINIZ

""")
while True:
    islem = input("İşlemi seçiniz")
    if(islem == "q"):
        print("Program sonlanıyor")
        break
    elif(islem == "1"):
        kumanda.tv_ac()
    elif(islem == "2"):
        kumanda.tv_kapat()
    elif(islem == "3"):
        kumanda.ses_ayarı()
    elif(islem == "4"):
        kanal_isimleri = input("Kanal isimlerini virgül ile ayırarak giriniz")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif(islem == "5"):
        print("Kanal Sayısı ",len(kumanda))
    elif (islem == "6"):
        kumanda.rastgele_kanal()
    elif (islem == "7"):
        print(kumanda)
    else:
        print("Geçersiz işlem")