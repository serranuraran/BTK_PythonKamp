yas=int(input("yasınızı giriniz:"))
if yas<18:
    print("üye olamazsınız")
else:
    print("üye olabilirsiniz")


#not ortalaması
not1=int(input("not 1 giriniz:"))
not2=int(input("not 2 giriniz:"))
ort=(not1+not2)/2
if ort>50:
    print("geçti")
else:
    print("kaldı")


#her iki not 60dan büyükse ortalama yazdırılsın
if not1>60 and not2>60:
    print(ort)
else:
    print("vizeye giremez")