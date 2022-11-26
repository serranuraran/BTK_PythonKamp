not1=int(input("not 1 giriniz:"))
not2=int(input("not 2 giriniz:"))

if(not1<0 or not1>100) or (not2<0 or not2>100):
    print("notla gecersiz")
else:
    ort=(not1+not2)/2
    if ort<50:
        print("kaldı")
    elif ort<70:
        print("orta")
    elif ort<85:
        print("iyi")
    else:
        print("pekiyi")
