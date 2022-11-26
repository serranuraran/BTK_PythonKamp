#hava durumu uygulaması
#hava sıcaklığını ekrandan alın
#sıcaklık sıfırdan küçükse "soğuk", 15te küçükse serin, 25ten küçükse "ılık", 35ten küçükse "sıcak", daha yüksekse "cok sıcak" yazsın


sicaklik=int(input("sıcaklık giriniz:"))
if sicaklik<-50 or sicaklik>100:
    print("sicaklik degeri anormal")
else:
    print("okunan sıcaklık degeri normal görünüyor")
    if sicaklik<0:
        print("soğuk")
    elif sicaklik<15:
        print("serin")
    elif sicaklik<25:
        print("ılık")
    elif sicaklik<35:
        print("sıcak")
    else:
        print("çok sıcak")