class Hayvanlar():
    def __init__(self,adı,soyadı,ayak_sayısı,cinsi,parmak_sayısı,dis_sayısı):
        self.adı = adı
        self.soyadı = soyadı
        self.cinsi = cinsi
        self.parmak_sayısı = parmak_sayısı
        self.ayak_sayısı= ayak_sayısı
        self.dis_sayısı = dis_sayısı
    def ad_ekle(self,ad):
        print("Hayvanın Adı:"+ad)
    def soyad_ekle(self,soyad):
        print("Hayvan Soyadı"+soyad)
    def ayak_sayısı_ekle(self,kac_ayak):
        print("Hayvanın ayak sayısı"+kac_ayak)
    def __str__(self):
        return "HAyvanın Adı{}\nHayvanın Soyadı{}\nKaç Ayaklı  {}".format(self.adı,self.soyadı,self.ayak_sayısı)
class Kopekler(Hayvanlar):
       def cins_fonk (self,cins):
           self.cinsi = cins
           print("Cinsi"+self.cins)
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
        hayvan1.ad_ekle()
    elif(islem == "2"):
        hayvan1.soyad_ekle()
    elif(islem == "3"):
        hayvan1.ayak_sayısı()
    elif (islem == "4"):
        hayvan1.cins()
    elif (islem == "5"):
        hayvan1.parmak_fonk()
    elif(islem == "6"):
        hayvan1.dis_sayısı()
    elif(islem == "7"):
        hayvan1.__str__()
    elif(islem == "q"):
        print("Programdan çıkılıyor")
        break
    else:
        print("Geçerli birşey giriniz")

