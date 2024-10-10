# Sayının tek mi çift mi olduğuna bakan ve onu yazdıran kod
# tekMiCiftMiSayi = int(input("Tek çift kontrolü için sayı girin: "))
# if tekMiCiftMiSayi % 2:
#     print(tekMiCiftMiSayi, "Sayiniz tek")
# else:
#     print(tekMiCiftMiSayi, "Sayiniz cift")

# Döngüler
# while:
# whileKosulu = 1
# while whileKosulu < 4:
#     print("Döngü", whileKosulu)
#     whileKosulu = whileKosulu + 1

# Faktöriyel Hesaplama:
# faktHesaplanacakSayi = input("Hangi sayinin faktöriyelini istersiniz? ")
# while faktHesaplanacakSayi == "":
#     faktHesaplanacakSayi = input("Lütfen bir sayı giriniz!")
# faktHesaplanacakSayi = int(faktHesaplanacakSayi)
#
# faktTutucu = 1
# while faktHesaplanacakSayi > 1:
#     faktTutucu = faktTutucu * faktHesaplanacakSayi
#     faktHesaplanacakSayi -= 1
# print(faktTutucu)

# iki sayı arasındaki çift sayıları sayan kod
# sayi1 = int(input("İlk sayıyı girin:"))
# sayi2 = int(input("İkinci sayıyı girin:"))
# sayac = 0
# kucuk_sayi = sayi1 + 1
# buyuk_sayi = sayi2
#
# if sayi1 > sayi2:
#     kucuk_sayi = sayi2 + 1
#     buyuk_sayi = sayi1
#
# while kucuk_sayi < buyuk_sayi:
#     if kucuk_sayi % 2 == 0:
#         sayac = sayac + 1
#     kucuk_sayi = kucuk_sayi + 1
# print(sayac)

# iki sayı arasındaki tek sayıları bulan ve ort alan fonksiyon
sayi1 = int(input("İlk sayıyı girin:"))
sayi2 = int(input("İkinci sayıyı girin:"))
sayac = 0
toplam = 0
kucuk_sayi = sayi1 + 1
buyuk_sayi = sayi2

if sayi1 > sayi2:
    kucuk_sayi = sayi2 + 1
    buyuk_sayi = sayi1

while kucuk_sayi < buyuk_sayi:
    if kucuk_sayi % 2:
        sayac = sayac + 1
        toplam = toplam + kucuk_sayi
    kucuk_sayi = kucuk_sayi + 1
print(toplam/sayac)
