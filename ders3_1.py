# Birden fazla değer tutmak için, liste kullanıyoruz.
liste = ["akif", "bülbül"]
# print(liste)

karisikListe = ["akif", 1, 3.4]
# print(karisikListe)
# print(karisikListe[0])

karisikListe[0] = 5
# print(karisikListe)

karisikListe.append(8) #Sona ekle
# print(karisikListe)

karisikListe.insert(0, "akif") #istenilen indexe ekle
# print(karisikListe)

karisikListe.pop() #Sondakini çıkart
# print(karisikListe)

karisikListe.remove("akif") #İstenilen değeri sil
# print(karisikListe)

karisikListe.pop(2) #İstenilen indexi çıkart
# print(karisikListe)

# print(len(karisikListe)) #Listenin boyutunu yazdırır

# 1 ile 20 arasındaki çift sayılardan oluşan bir liste oluşturan kodu yazın

sayilarListesi = []
for k in range(2, 20, 2):
    sayilarListesi.append(k)
# for eleman in sayilarListesi:
#     print(eleman)

# Kullanıcının girmiş olduğu 2 değer arasındaki 3'e bölünen sayılardan oluşan
# listenin ortalamasını hesaplayan ve sonucu yazdıran kodu yazın

sayi1 = int(input("ilk sayı:"))
sayi2 = int(input("ikinci sayı:"))
ucunKatlari = []
sayac = 0
toplam = 0
kucuk_sayi = sayi1 + 1
buyuk_sayi = sayi2

if sayi1 > sayi2:
    kucuk_sayi = sayi2 + 1
    buyuk_sayi = sayi1
for i in range(kucuk_sayi, buyuk_sayi):
    if i % 3 == 0:
        ucunKatlari.append(i)
sayac = len(ucunKatlari)
for eleman in ucunKatlari:
    toplam = toplam + eleman
if sayac == 0:
    print("Girilen 2 sayı arasında hiç 3ün katı yok!")
else:
    print("Ortalama =", toplam / sayac)