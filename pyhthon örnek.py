araba = int(input("Otoparkta Kaç Araba Var: "))
boş_yer = int(input("Otoparkta Kaç Boş Yer Var:"))

while True:
    otopark = int(input("1 - Giriş, 2 - Çıkış, 3 - Çıkış Yap: "))

    if otopark == 1:
        if boş_yer > 0:
                araba += 1
                boş_yer -=1
        print("Araba Giriş Yapılıyor:")
        # araba += 1, boş_yer -= 1 (taşma kontrolü yap)
    elif otopark == 2:
        if araba > 0:
             araba -= 1
             boş_yer +=1
        print("Araba Çıkış Yapılıyor:")
        # araba -= 1, boş_yer += 1 (negatif olmasın)
    elif otopark == 3:
        print("Programdan Çıkış Yapılıyor")
        break
    else:
        print("Geçersiz Seçim, Tekrar Deneyin:")

    # her tur sonunda durumu göster:
    print("Kalan Boş Yer Sayısı:", boş_yer, " | Otoparktaki Araba:", araba)
