
sekil = input("Üçgenin mi tipini bulmak istersiniz Dörtgenin mi ?")
if(sekil == "Dörtgen"):
    a = int(input("Birinci kenarı Giriniz"))
    b = int(input("Birinci kenarı Giriniz"))
    c = int(input("Birinci kenarı Giriniz"))
    d = int(input("Birinci kenarı Giriniz"))
    if(a == b and a == c and a == d):
        print("Bu bir Karedir")
    elif(a == c and b == d):
        print("Dikdörtgen")
    else:
        print("Rastgele dörtgenddir")
elif(sekil == "Üçgen"):
    a = abs(int(input("Birinci Kenarı görünüz")))
    b = abs(int(input("İkinci kenarı giriniz")))
    c = abs(int(input("Üçüncü kenarı giriniz")))
    if(a == b and a == c):
        print("Eşkenar Üçgendir")
    elif(a == b or a==c  ):
        print("İkizkenar Üçndir")
    elif(b == a or b==c):
        print("İkizkenar Üçgen")
    else:
        print("Rastgele Üçgendir")

