import random
# 0 ila 1 arasında rastgele bir sayı üretir
randSayi1 = random.random()
# print(randSayi1)
#50 ila 60 arasında rastgele bir sayı üretir
randSayi2 = random.uniform(50,60)
# print(randSayi2)
#50 ila 100 arasında rastgele bir integer üretir
randSayi3 = random.randint(50, 100)
# print(randSayi3)

#Kullanıcıların girmiş olduğu tam sayı değerler arasından rastgele 5 elemandan oluşan bir listenin,
#elemanlarını gösteriniz ve ortalamasını alınız.

sayi1 = int(input("1. sayi gir"))
sayi2 = int(input("2. sayi gir"))
sayac = 0; toplam = 0
kucuk_sayi = sayi1 + 1
buyuk_sayi = sayi2 - 1
rastgele_sayilar = []

if sayi1 > sayi2:
    kucuk_sayi = sayi2 + 1
    buyuk_sayi = sayi1 - 1

if (buyuk_sayi + 1) - (kucuk_sayi - 1) <= 1:
    print("Sayılar arasında random sayı üretilemiyor. Sayılar arasındaki farkı arttırın!")
else:
    for i in range(5):
        randomEleman = random.randint(kucuk_sayi, buyuk_sayi)
        rastgele_sayilar.append(randomEleman)
        toplam = toplam + randomEleman
    sayac = len(rastgele_sayilar)
    print("Rastgele liste:", rastgele_sayilar)
    print("Ortalaması:", toplam/sayac)