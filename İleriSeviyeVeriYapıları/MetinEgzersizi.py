class Dosya():
    def __init__(self):
        with open("metin.txt","r",encoding="utf-8")as file:
            dosya_icerigi = file.read()
            kelimeler = dosya_icerigi.split()
            self.sade_kelimeler = list()
            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(",")
                i = i.strip(".")
                self.sade_kelimeler.append(i)
    def tüm_kelimeler(self):
        kelimeler_kumesi = set()
        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i)
        print("TÜm kelimeler....")
        for i in kelimeler_kumesi:
            print(i)
            print("***********************")
    def kelime_frekansı(self):
        kelime_sözlük = dict()
        for i in self.sade_kelimeler:
            if(i in kelime_sözlük):
                kelime_sözlük[i]+=1
            else:
                kelime_sözlük[i] = 1
        for kelime,sayi in kelime_sözlük.items():
            print("{} kelimesi {} kere geçiyor".format(kelime,sayi))
            print("***************")
dosya = Dosya()
dosya.tüm_kelimeler()
dosya.kelime_frekansı()