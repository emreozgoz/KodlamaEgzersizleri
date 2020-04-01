class Hayvanlar():
    def __init__(self,adı,soyadı,ayak_sayısı,cinsi,parmak_sayısı,dis_sayısı):
        self.adı = adı
        self.soyadı = soyadı
        self.cinsi = cinsi
        self.parmak_sayısı = parmak_sayısı
        self.ayak_sayısı= ayak_sayısı
        self.dis_sayısı = dis_sayısı
    def ad_ekle(self,ad):
        self.adı = ad
        print("Hayvanın Adı:"+ad)
    def soyad_ekle(self,soyad):
        self.soyadı =soyad
        print("Hayvan Soyadı"+soyad)
    def ayak_sayısı_ekle(self,kac_ayak):
        self.ayak_sayısı == kac_ayak
        print("Hayvanın ayak sayısı"+kac_ayak)
    def __str__(self):
        return "HAyvanın Adı{}\nHayvanın Soyadı{}\nKaç Ayaklı  {}\n,Cinsi{}\n Parmak Sayısı{}\nDiş Sayısı{}".format(self.adı,self.soyadı,self.ayak_sayısı,self.cinsi,self.parmak_sayısı,self.dis_sayısı)
class Kopekler(Hayvanlar):
       def cins_fonk (self,cins):
           self.cinsi = cins
           print("Cinsi"+cins)
class Kuslar(Hayvanlar):
    def parmak_fonk(self, parmak):
        self.parmak_sayısı = parmak
        print("HAyvanın parmak Sayısı" + parmak)
class At(Hayvanlar):
    def dis_fonk(self,disinin_sayisi):
        self.dis_sayısı = disinin_sayisi
        print("Dişinin Sayısı"+disinin_sayisi)
hayvan1 = Hayvanlar("Karabaş","Çomar",4,"Doberman",4,15)
while True:
    islem = input("""
    1-Ad Ekle
    2-Soyad Ekle
    3-Ayak Sayısı Ekle
    4-Cinsi Ekle
    5-Parmak Ekle
    6-Dis Ekle
    7-Genel Bilgi 
    Çıkış için q ya basınız
    
    
    
    
    
    """)
    if(islem == "1"):
        ad = input("Adını Ne ile Değiştirmek istersiniz ? ")
        hayvan1.ad_ekle(ad)
    elif(islem == "2"):
        soyad = input("Soyadını Ne ile Değiştirmek istersiniz ? ")
        hayvan1.soyad_ekle(soyad)
    elif(islem == "3"):
        ayak_sayısı = input("Ayak Sayısı Kaç olsun ? ")
        hayvan1.ayak_sayısı = ayak_sayısı
    elif (islem == "4"):
        cinsii = input("Cinsini Ne ile Değiştirmek istersiniz ? ")
        hayvan1.cins_fonksiyon(cinsii)
    elif (islem == "5"):
        parmak = input("Parmak sayısı Ne ile Değiştirmek istersiniz ? ")
        hayvan1.parmak_fonk(parmak)
    elif(islem == "6"):
        dis = input("Siş Sayısı Ne ile Değiştirmek istersiniz ? ")
        hayvan1.dis_sayısı(dis)
    elif(islem == "7"):
        print(hayvan1)
    elif(islem == "q"):
        print("Programdan çıkılıyor")
        break
    else:
        print("Geçerli birşey giriniz")

