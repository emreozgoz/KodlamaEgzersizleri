username = "emreozgoz"
passw= 123456

print("Hoşgeldiniz Lütfen Kullanıcı adınızı ve şifrenizi giriniz")
a = input("Kullanıcı adınızı giriniz")
b = int(input("Şifrenizi Giriniz "))
if (a!= username and b== passw):
    print("Kullanıcı adınız hatalı")
if   (a != username and b != passw):
     print("Kullanıcı adı ve Parolanız hatalı")
if (a == username and b != passw):
    print("Hatalı Şifre")
elif(a == username and b == passw):
    print("Başarıyla giriş yaptınız")