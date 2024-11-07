# Kullanıcının girmiş olduğu tamsayı değerleri arasından yine kullanıcının girmiş olduğu
# değer kadar rastgele tam sayılardan oluşan listeyi ve listenin en büyük elemanını yazdır

import random

sayi1 = int(input("1. sayi gir "))
sayi2 = int(input("2. sayi gir "))
sayi3 = int(input("Kaç rastgele sayı olsun "))
kucuk_sayi = sayi1 + 1
buyuk_sayi = sayi2 - 1
rastgele_sayilar = []

if sayi1 > sayi2:
    kucuk_sayi = sayi2 + 1
    buyuk_sayi = sayi1 - 1

if (buyuk_sayi + 1) - (kucuk_sayi - 1) <= 1:
    print("Sayılar arasında random sayı üretilemiyor. Sayılar arasındaki farkı arttırın!")
elif sayi3 == 0:
    print("Rastgele sayi oluşturulmadı")
else:
    for i in range(sayi3):
        randomEleman = random.randint(kucuk_sayi, buyuk_sayi)
        rastgele_sayilar.append(randomEleman)
    print("Rastgele liste:", rastgele_sayilar)
    enBuyukEleman = rastgele_sayilar[0]
    for eleman in rastgele_sayilar:
        if eleman > enBuyukEleman:
            enBuyukEleman = eleman
    print("En büyük eleman =", enBuyukEleman)
