a = int(input("Toplama için 1:\nÇıkarma için 2:\nÇarpma için 3:\nBölme için 4:"))
num1 = int(input("Birinci Sayıyı Giriniz"))
num2 = int(input("İkinci Sayıyı Giriniz"))

if (a ==1):
    print("{} + {} = {}".format(num1,num2,num1+num2))
elif(a == 2):
    print("{} - {} = {}".format(num1,num2,num1-num2))
elif (a == 3):
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif(a == 4):
    print("{} - {} = {}".format(num1,num2,num1/num2))
else:
    print("Geçerli bir işlem giriniz")



