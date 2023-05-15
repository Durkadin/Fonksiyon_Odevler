min_sayi = int(input("minimum sayiyi giriniz .."))
max_sayi = int(input("maximum sayiyi giriniz .."))
bolen_sayi = int(input("bolen sayiyi giriniz .."))
tam_bolunenler = []


def bolunen_sayi_bulma(min_sayi, max_sayi, bolen_sayi) :

     sayi_sayac = 0

     for i in range(min_sayi,max_sayi):
         if(i % bolen_sayi == 0):
           tam_bolunenler.append(i)
           sayi_sayac += 1

     print("Bolunen Sayilar", tam_bolunenler)
     print("Bolunen Toplam Sayi", sayi_sayac)    
    
print(bolunen_sayi_bulma(min_sayi,max_sayi,bolen_sayi))
     
