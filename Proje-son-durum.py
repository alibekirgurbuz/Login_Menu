while True:
    secim = input("Lütfen birini seçin:\n1-Sisteme Üye Ol\n2-Sisteme Giriş Yap\n3-Şifremi Unuttum\nSeçiminiz: ")
    if secim == "1":
        print("Sisteme üye olma işlemleri yapılıyor.")
        ad = input("Adınız: ")
        soyad = input("Soyadınız: ")
        kullanici_adi = input("Kullanıcı adı: ")
        sifre = input("Şifre: ")

        with open("kullanicilar.txt", "a") as dosya:
            dosya.write(kullanici_adi + "," + sifre + "," + ad + "," + soyad + "\n")

        print("Kaydınız oluşturuldu. Giriş yapabilirsiniz.")
        break
    elif secim == "2":
        print("Sisteme giriş yapma işlemleri yapılıyor.")
        kullanici_adi = input("Kullanıcı adı: ")
        sifre = input("Şifre: ")
        with open("kullanicilar.txt", "r") as dosya:
            kullanicilar = dosya.readlines()
            for kullanici in kullanicilar:
                bilgiler = kullanici.strip().split(",")
                if kullanici_adi == bilgiler[0] and sifre == bilgiler[1]:
                    print("Giriş başarılı. Hoş geldiniz,", bilgiler[2], bilgiler[3])
                    def TCKONTROL():
                        while True:
                            TC = input("Lütfen TC kimlik numaranızı girin: ")
                            if len(TC) != 11:
                                print("Hata: TC kimlik numarası 11 haneden oluşmalıdır!")
                            else:
                                with open("notlar.txt", "a") as dosya:
                                    dosya.write("TC Kimlik No: " + TC + "\n")
                                break                        
                    def isimleri_kaydet():
                        isimler = []
                        while True:
                            isim = input("Kaydetmek istediğiniz ismi girin (Çıkmak için Q tuşuna basın): ")
                            if isim.lower() == "q":
                                break
                            isimler.append(isim)    
                            with open("notlar.txt", "a") as dosya:
                                for isim in isimler:
                                    dosya.write("İsim: " + isim + "\n")
                                print("İsimler başarıyla kaydedildi!")  
                    def telno():
                        while True:
                            telefon_no = input("Lütfen telefon numaranızı girin: ")
                            if len(telefon_no) != 10 or telefon_no.startswith("0"):
                                print("Hata: Telefon numarası 10 haneli ve başında sıfır olmadan girilmelidir!")
                            else:
                                with open("notlar.txt", "a") as dosya:
                                    dosya.write("Telefon No: " + telefon_no + "\n")
                                break
                    def konumları_kaydet():
                        with open("konumlar.txt", "a") as dosya:
                            il = input("Lütfen ilinizi girin: ")
                            dosya.write("İl: " + il + "\n")
                            ilce = input("Lütfen ilçenizi girin: ")
                            dosya.write("İlçe: " + ilce + "\n")
                            mahalle = input("Lütfen mahallenizi girin: ")
                            dosya.write("Mahalle: " + mahalle + "\n")
                        print("Konum bilgileri başarıyla kaydedildi!")
                    TCKONTROL()
                    isimleri_kaydet()
                    telno()
                    konumları_kaydet()
                    break
            else:
                print("Kullanıcı adı veya şifre yanlış. Lütfen tekrar deneyin.")
    elif secim == "3":
        print("Şifremi unuttum işlemleri yapılıyor.")
        kullanici_ad = input("Kullanıcı adınızı girin: ")
        with open("kullanicilar.txt", "r") as dosya:
            kullanicilar = dosya.readlines()
        for kullanici in kullanicilar:
            bilgiler = kullanici.strip().split(",")
            if kullanici_ad == bilgiler[0]:
                yeni_sifre = input("Yeni şifrenizi girin: ")
                kullanicilar.remove(kullanici)
                kullanicilar.append(kullanici_ad + "," + yeni_sifre + "," + bilgiler[2] + "," + bilgiler[3] + "\n")
                with open("kullanicilar.txt", "w") as dosya:
                    dosya.writelines(kullanicilar)
                print("Şifreniz değiştirildi!")
                break
        else:
            print("Kullanıcı adı yanlış!")
    else:
        print("Geçersiz bir seçim yaptınız. Lütfen seçenek seçiniz.")
        #Son Durum