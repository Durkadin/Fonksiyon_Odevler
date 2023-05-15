def deger_kontrol(notu):
    if(notu >=1 and notu <= 100):
        return sinav_notu.append(notu)
        
    else :
         print("Girmiş olduğunuz değer geçerli aralıkta değildir!! Lütfen 1-100 arasında bir deüer giriniz:")
         notu = int(input("Lütfen sınav notunu girin :"))
         deger_kontrol(notu)

sinav_notu = []
vize1 = float(input("Vize 1 değerini giriniz "))
deger_kontrol(vize1)
vize2 = float(input("Vize 2 değerini giriniz "))
deger_kontrol(vize2)
final = float(input("Final değerini giriniz "))
deger_kontrol(final)


genel_not = (sinav_notu[0] * 30 / 100) + (sinav_notu[1] * 30 / 100) + (sinav_notu[2] * 40 / 100)

print("Genel not ortalamanız :", genel_not)

if (genel_not >= 90):
    print("AA")
elif (genel_not >= 85):
    print("BA")
elif (genel_not >= 80):
    print("BB")
elif (genel_not >= 75):
    print("CB")
elif (genel_not >= 70):
    print("CC")
elif (genel_not >= 65):
    print("DC")
elif (genel_not >= 60):
    print("DD")
elif (genel_not >= 55):
    print("FD")
else:
    print("FF")
