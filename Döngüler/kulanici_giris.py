sys_kullaniciadi ="emreozgoz"
sys_pass = "1234"
giris_hakki = 3

while True:

    kullanici_adi = input("Kullanıcı adınızı giriniz:")
    kullanici_pass = input("Şifrenizi Giriniz")
    if(kullanici_adi == sys_kullaniciadi and kullanici_pass == sys_pass):
            print("Tebrikler Başarıyla giriş yaptınız")
            break
    elif(kullanici_pass == sys_pass and kullanici_adi != sys_kullaniciadi):
            print("Kullanıcı adınız Yanlış")
            giris_hakki -= 1
    elif(kullanici_pass != sys_pass and kullanici_adi == sys_kullaniciadi):
            print("Parolanız yanlış")
            giris_hakki -=1
    elif(kullanici_pass != sys_pass and kullanici_adi != sys_kullaniciadi):
            print("Kullanıcı adı ve şifreniz hatalı")
            giris_hakki -= 1
    if(giris_hakki == 0):
            print("Giriş hakknıız kalmamıştır")
            break

