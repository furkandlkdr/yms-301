# For döngüsü:

#0'dan 5'e kadar 5 dahil dğeil
# for i in range(5):
#     print(i)
#
# 5ten 10'a kadar 10 dahil değil
# for j in range(5,10):
#     print(j)
#
# 1'den 20'ye kadar 4'erli artış şeklinde 20 dahil değil
# for k in range(1,20,4):
#     print(k)

# sayi1 = int(input("İlk sayıyı girin:"))
# sayi2 = int(input("İkinci sayıyı girin:"))
# sayac = 0
# toplam = 0
# kucuk_sayi = sayi1 + 1
# buyuk_sayi = sayi2
#
# if sayi1 > sayi2:
#     kucuk_sayi = sayi2 + 1
#     buyuk_sayi = sayi1
#
# for i in range(kucuk_sayi, buyuk_sayi):
#     if i % 2:
#         sayac = sayac + 1
#         toplam = toplam + i
# print(toplam/sayac)

# (3x + 4y) / (z! - 3t) fonksiyonunu hesaplayan programı yaz. Kontrolleri sağla
degiskenX = ""
degiskenY = ""
degiskenZ = ""
degiskenT = ""
sonuc = 0

print("(3x + 4y) / (z! - 3t) fonksiyonu için:")
while degiskenX == "":
    degiskenX = input("X")
degiskenX = int(degiskenX)
while degiskenY == "":
    degiskenY = input("Y")
degiskenY = int(degiskenY)
while degiskenZ == "":
    degiskenZ = input("Z")
degiskenZ = int(degiskenZ)
while degiskenT == "":
    degiskenT = input("T")
degiskenT = int(degiskenT)

zFaktoriyel = 1
for fakt in range(1, degiskenZ + 1):
    zFaktoriyel = zFaktoriyel * fakt

if zFaktoriyel - (3*degiskenT) == 0:
    print("Payda SIFIR oldu, tanımsızdır!")
else:
    sonuc = ( (3*degiskenX) + (4*degiskenY) ) / (zFaktoriyel - (3*degiskenT))
    print("(3 *", degiskenX, "+ 4 *", degiskenY,  ") / (", zFaktoriyel, "- ", "( 3 *", degiskenT ,") = ", sonuc)
