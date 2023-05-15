Birlikler = ["bir","iki","uc","dort","bes","altı","yedi","sekiz","dokuz"]
Onluklar = ["on","yirmi","otuz","kırk","elli","altmış","yetmis","seksen","doksan"]
def sayi_okunusu(atanan_sayi):
    print(Onluklar[int(atanan_sayi/10)-1]  + "" + Birlikler[int(atanan_sayi % 10)-1])

def sayi_atama(ikibasamaklisayi):
    if(ikibasamaklisayi >= 10 and ikibasamaklisayi <= 99):
        atanan_sayi=ikibasamaklisayi
        sayi_okunusu(ikibasamaklisayi)
    
    else:
        print(" Yanlış sayı girdiniz!!.Bu sebeple sizi bu sistemden cikariyorum")
        exit()

def main():
    ikibasamaklisayi = int(input("Iki basamaklı bir sayi giriniz .."))
    sayi_atama(ikibasamaklisayi)

if __name__ == '__main__':
    main()