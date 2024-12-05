# Kullanıcının girmiş olduğu değerler arasında yine kullanıcının girmiş olduğu değer kadar
# rastgele elemanlardan oluşan bir listede görmüş olduğunuz istatistiki bilgileri yazdiriniz
import random
from statistics import *

sayi1 = int(input("İlk sayıyı girin:"))
sayi2 = int(input("İkinci sayıyı girin:"))
listeBoyutu = int(input("Kaç elemanlı bir liste olsun:"))
buyuk_sayi = sayi1
kucuk_sayi = sayi2
sayiListesi = []
sayiListesi2 = []
if sayi2 > sayi1:
    buyuk_sayi = sayi2
    kucuk_sayi = sayi1
for i in range(listeBoyutu):
    sayiListesi.append(random.randint(kucuk_sayi, buyuk_sayi))
    sayiListesi2.append(random.randint(kucuk_sayi, buyuk_sayi))
print('Sayi listesi:', sayiListesi)
print('Sayi listesi2:', sayiListesi2)
print('Ort:', mean(sayiListesi))

engelVarMi = False
for i in range(listeBoyutu):
    if sayiListesi[i] == 0 or sayiListesi2[i] == 0:
        engelVarMi = True
    elif sayiListesi[i] < 0 or sayiListesi2[i] < 0:
        engelVarMi = True
if engelVarMi == False:
    print('Harm.:', harmonic_mean(sayiListesi), 'Geo:', geometric_mean(sayiListesi))
else:
    print("Sıfır içerdiği için geometrik ve harmonik hesaplanamıyor")

#Sırala
for i in range(listeBoyutu):
    for j in range(i+1, listeBoyutu-1):
        if sayiListesi[i] > sayiListesi[j]:
            temp = sayiListesi[i]
            sayiListesi[i] = sayiListesi[j]
            sayiListesi[j] = temp
        if sayiListesi2[i] > sayiListesi2[j]:
            temp = sayiListesi2[i]
            sayiListesi2[i] = sayiListesi2[j]
            sayiListesi2[j] = temp

print("Sıralı diziler:\n", sayiListesi, "\n", sayiListesi2)
print('Mod:', mode(sayiListesi), 'Med:', median(sayiListesi),
      'Var:', variance(sayiListesi), 'ss:', stdev(sayiListesi))
print('Kov:', covariance(sayiListesi, sayiListesi2), 'cor:', correlation(sayiListesi, sayiListesi2))
b, a = linear_regression(sayiListesi, sayiListesi2)
print('Lineer için a:', a, 'b:', b)
