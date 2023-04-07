while True:
    secim = input("Lütfen bir seçenek seçin:\n1-Sisteme Üye Ol\n2-Sisteme Giriş Yap\n3-Şifremi Unuttum\nSeçiminiz: ")

    if secim == "1":
       
        print("Sisteme üye olma işlemleri yapılıyor...")
        ad = input("Adınız: ")
        soyad = input("Soyadınız: ")
        kullanici_adi = input("Kullanıcı adı: ")
        sifre = input("Şifre: ")

        with open("kullanicilar.txt", "a") as dosya:
            dosya.write(kullanici_adi + "," + sifre + "," + ad + "," + soyad + "\n")
        
        print("Kaydınız başarıyla oluşturuldu. Giriş yapabilirsiniz.")
        break

    elif secim == "2":
        
        print("Sisteme giriş yapma işlemleri yapılıyor...")
        kullanici_adi = input("Kullanıcı adı: ")
        sifre = input("Şifre: ")

        with open("kullanicilar.txt", "r") as dosya:
            kullanicilar = dosya.readlines()

        for kullanici in kullanicilar:
            bilgiler = kullanici.strip().split(",")
            if kullanici_adi == bilgiler[0] and sifre == bilgiler[1]:
                print("Giriş başarılı. Hoş geldiniz,", bilgiler[2], bilgiler[3])
                break
        else:
            print("Kullanıcı adı veya şifre yanlış. Lütfen tekrar deneyin.")

    elif secim == "3":
        
        print("Şifremi unuttum işlemleri yapılıyor...")
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

                print("Şifreniz başarıyla değiştirildi!")
                break
        else:
            print("Kullanıcı adı yanlış!")

    else:
        print("Geçersiz bir seçim yaptınız. Lütfen seçenek seçiniz.")


