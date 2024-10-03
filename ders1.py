print("Merhaba Dünya!")
# Açıklama satırları

# Değişkenler
a = 5
b = 'true'
c = 4.56
d = "akif"
print("Değişken değeri:", d)

# Aritmatik işlemler
# + - * / %
sayi1 = 7
sayi2 = 4
snc = sayi1 % sayi2
print("Mod sonucu:", snc)

# Karşılaştırma operatörleri
# < > <= >= == !=

# Kullanıcıdan bilgi alma
# veri = input("Lütfen Adınızı Girin : ")
# print("Girilen değer:", veri)
# veri2 = int(input("Bir sayi girin : "))
# print("Girilen sayi:", veri2, type(veri2))
# veri3 = float(input("Lütfen ondalıklı sayı girin : "))
# print("Ondalıklı sayı:", veri3)
# x = int(input("İlk sayıyı girin: "))
# y = int(input("İkinci sayıyı girin: "))
# print("Çarpım: ", x * y)
# print("Bölüm: ", x / y)
# print("Toplam: ", x + y)
# print("Çıkarma: ", x - y)

#if blokları
if (4>5):
    print("if blogu")
elif(5==5):
    print("elif dedin usta")
else:
    print("else blogu")

ilkSayi = int(input("Bir sayi girin : "))
ikinciSayi = int(input("Bir sayi girin : "))

if (ilkSayi > ikinciSayi):
    print("ilkSayi büyüktür")
elif (ilkSayi < ikinciSayi):
    print("ikinciSayi büyüktür")
else:
    print("eşittir")

