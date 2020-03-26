vize1 = int(input("Vize Notunuzu Giriniz"))
vize2 = int(input("İkinci Vize Notunuzu Giriniz"))
final= int(input("Final Notunuzu Griiniz"))
vize1 = vize1*0.30
vize2 = vize2*0.30
final = final*0.40
toplam = vize1+vize2+final
if(toplam>=90):
    print("AA")
elif(toplam>=85):
    print("BA")
elif(toplam>=80):
    print("BB")
elif(toplam>=75):
    print("CB")
elif(toplam>=70):
    print("CC")
elif(toplam>=65):
    print("DC")
elif(toplam>=60):
    print("DD")
elif(toplam>=55):
    print("FD")
elif(toplam<50):
    print("FF")