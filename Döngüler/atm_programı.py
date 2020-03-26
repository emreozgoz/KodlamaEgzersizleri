bakiye = 1000
while True:
    islem = input("Bakiye Sorgulama için 1 \n Para Yatırma için 2 \n PAra çekme için 3 e basınız\n Çıkmak için q ya basınız")
    if (islem == "q"):
        break
    if(islem == "1"):
        print(bakiye)

    elif(islem == "2" ):
        yatirilan = int(input("Ne kadar yatıracaksınız"))
        bakiye += yatirilan
        print(bakiye)

    elif(islem == "3" ):
        cekilen = int(input("Ne kadar çekeceksiniz"))
        if(cekilen>bakiye):
            print("Atmde o kadar para yok")
            continue
        else:
         bakiye -= cekilen
        print(bakiye)
    else:
        print("Geçerli işlem giriniz")
