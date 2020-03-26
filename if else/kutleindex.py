length = int(input("Boyunuzu Giriniz:"))
weight = int(input("Kilonuzu Giriniz:"))
length = length*0.01
index = weight / (length*length)
if(index<18.5):
    print("Zayıfsınız...")
elif(18.5<index<25):
    print("Normal...")
elif(25<index<30):
    print("Fazla Kilolu")
elif(index>30):
    print("Obez:")
