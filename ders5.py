import random

def fnk_liste_islemi(a):
    a[0] = 1
    return a

# Parametre olarak almış olduğu 2 değer arasında yine parametre olarak almış olduğu
# boyut kadar rastgele elemanlardan oluşan bir liste oluşturan ve bu listeyi geri dönderen fonk yaz
def fnk_random_liste(say1, say2, boyut):
    buyuk_say = say1 - 1
    kucuk_say = say2 + 1
    if say1 < say2:
        buyuk_say = say2 - 1
        kucuk_say = say1 + 1
    if boyut < 1:
        print("Liste oluşturulamadı")
    elif buyuk_say - kucuk_say < 1:
        print("Liste oluşturulamadı")
    sayiListesi = []
    for i in range(boyut):
        sayiListesi.append(random.randint(kucuk_say, buyuk_say))
    return sayiListesi

# sayi1 = int(input("1. sayi gir "))
# sayi2 = int(input("2. sayi gir "))
# sayi3 = int(input("Kaç rastgele sayı olsun "))
#
# print(fnk_random_liste(sayi1, sayi2, sayi3))

# Parametre olarak almış olduğu 2 listeden, liste elemanlarından en büyük sayıyı bulan
# ve sonucu geri dönderen bir fonksiyon yazınız ve kullanınız.

def fnk_liste_maks_bul(list1, list2):
    maks = 0
    if len(list1) == 0 and len(list2) == 0:
        print("Listeler boş!")
        return 0
    maksLen = len(list1)
    if len(list1) == 0:
        maks = list2[0]
    else:
        maks = list1[0]
    if len(list2) > len(list1):
        maksLen = len(list2)
    for i in range(maksLen):
        if i < len(list2):
            if maks < list2[i]:
                maks = list2[i]
        elif i < len(list1):
            if maks < list1[i]:
                maks = list1[i]
    return maks

list1 = [4214,132,11,-11,1000]
list2 = [-1231, 12321, 111, 111, 1000]
print(fnk_liste_maks_bul(list1, list2))
