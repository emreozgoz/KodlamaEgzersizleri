import time
class Bilgisayar():
    def __init__(self,durum ="Kapalı",parlaklık = 0,programlar =["Chrome","LOL"],ack_program = "Chrome"):
        self.durum = durum
        self.parlaklık = parlaklık
        self.programlar = programlar
        self.ack_program = ack_program
    def pc_ac(self):

        if(self.durum == "Kapalı"):
            print("Bİlgisayar açılıyor")
            time.sleep(1)
            self.durum = "Açık"
        else:
            print("Bilgisayar Zaten açık")
    def pc_kapat(self):
        if(self.durum == "Açık"):
            print("Bilgisayar kapanıyor")
            time.sleep(1)
            self.durum = "Kapalı"
        else:
            print("Bilgisayar zaten kapalı")
    def parlaklık_ayarı(self):

        parlaklık_islem = input("Arttırmak için + Azaltmak için - Tuşuna basın")
        if(parlaklık_islem == "+"):
            print("Parlaklık arttırılıyor")
            self.parlaklık +=1
            print(self.parlaklık)
        elif(parlaklık_islem == "-"):
            if(self.parlaklık == 0):
                print("Parlaklık daha fazla düşürülemez")
            elif(self.parlaklık>0):
                print("Parlaklık azaltılıyor")
                self.parlaklık -= 1
            print(self.parlaklık)

    def program_ekle(self,program_isim):
        self.programlar.append(program_isim)
    def __str__(self):
        return "Pc durumu {}\nPC parlaklık:{}\n,Açık programlar:{}".format(self.durum,self.parlaklık,self.programlar)
    def __len__(self):
        return  len(self.programlar)

bilgisayar = Bilgisayar()
while True:
    islem = input("""
    1-PC AÇ
    2-PC KAPAT
    3-PARLAKLIK AYARI
    4-PROGRAM EKLE
    5-PROGRAM SİL
    6-GENEL DURUM
    7-PROGRAMLAR
    
    
    
    
    """)
    if(islem == "1"):
        bilgisayar.pc_ac()
    elif(islem == "2"):
        bilgisayar.pc_kapat()
    elif(islem == "3"):
        bilgisayar.parlaklık_ayarı()
    elif(islem == "4"):
        program_adıı= input("Eklemek istediğiniz programı yazınız")

        bilgisayar.program_ekle(program_adıı)

    elif(islem == "6"):
        print(bilgisayar)
    elif(islem == "7"):
      print(  len(bilgisayar))
    elif(islem == "q"):
        print("Programdan çıkılıyor.....")
        break
    else:
        print("Geçerli birşey giriniz")