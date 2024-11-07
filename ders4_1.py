# Kullanıcının girmiş olduğu değerler arasında girilen değerler dahil yine kullanıcının girmiş
# olduğu boyut kadar tekrarsız bir liste oluşturan kodları yazınız. Listeyi yazdırın
import random

sayi1 = int(input("İlk sayıyı girin:"))
sayi2 = int(input("İkinci sayıyı girin:"))
listeBoyutu = int(input("Kaç elemanlı bir liste olsun:"))
buyuk_sayi = sayi1
kucuk_sayi = sayi2
sayiListesi = []
if sayi2 > sayi1:
    buyuk_sayi = sayi2
    kucuk_sayi = sayi1
fark = (buyuk_sayi - kucuk_sayi + 1) / 2

if fark < listeBoyutu:
    print("Aradaki fark uygun liste oluşturmaya yetmiyor!")
elif  listeBoyutu < 1:
    print("Rastgele sayı oluşturulamadı")
else :
    sayac = 0
    while sayac < listeBoyutu:
        rastgele_sayi = random.randint(kucuk_sayi, buyuk_sayi)
        rastgeleHataliMi = False
        if rastgele_sayi % 2 == 0:
            rastgeleHataliMi = True
        else:
            for el in sayiListesi:
                if el == rastgele_sayi:
                    rastgeleHataliMi = True
            if rastgeleHataliMi == False:
                sayiListesi.append(rastgele_sayi)
                sayac = sayac + 1
    # for i in range(listeBoyutu):
    #     randomEleman = 0
    #     istenmeyenVar = True
    #     while istenmeyenVar:
    #         randomEleman = random.randint(kucuk_sayi, buyuk_sayi)
    #         istenmeyenVar = False
    #         if randomEleman % 2 == 0:
    #             istenmeyenVar = True
    #         for el in sayiListesi:
    #             if randomEleman == el:
    #                 istenmeyenVar = True
    #     sayiListesi.append(randomEleman)
    print(sayiListesi)
