"""
#0-5 arası sayıları yazdır
for sayi in range(0,6):
    print(sayi)

#1-5 arası sayılar
for x in range(1,6):
    print(x)

#0-20 arası çift sayıları yazdır
for ciftsayi in range(0,21,2):
    print(ciftsayi)

toplam=0
for x in range(1,6):
    toplam=x+toplam
print("toplam=",toplam)


toplam=0
x=1
while x<=5:
     toplam=x+toplam
     print("toplam=",toplam)
     x=x+1

"""
# 1-100 arası çift sayıların toplamı?
toplam=0
for x in range(1,101,2):
    toplam=x+toplam
print("toplam=",toplam)

toplam=0
i=1
while i<=100:
    toplam=toplam+i
    print("toplam=",toplam)
    i=i+2