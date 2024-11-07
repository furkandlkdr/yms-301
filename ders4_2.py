# Fonksiyonlar
# Aynı görev ve kodları tekrar tekrar yazmamak için görev yerine getirmeye yarayan kod blokları

def fnk_mesaj(): # Parametresiz ve geriye değer döndermeyen fonksiyon
    print("Merhaba, Dünya!")

def fnk_mesaj_par(a): # Parametreli, geriye değer döndermeyen
    print(a)

def fnk_mesaj_par_top(a,b): # Parametreli, geriye değer dönderen
    c = a + b
    return c

# fnk_mesaj()
# fnk_mesaj_par("Selam dünya")
# return_degeri = fnk_mesaj_par_top("Hello ", "World")
# fnk_mesaj_par(return_degeri)

# Parametre olarak aldığı iki değeri toplayan ve sonucu geri dönderen
# Parametre olarak aldığı iki değerin farkını alan ve sonucu geri dönderen
# Parametre olarak aldığı iki değerin çarpımını bulan ve geri dönderen
# '' bölümünü bulan ve geri dönderen
# Parametre olarak aldığı değeri ekrana yazdıran fonksiyonu yaz
# (2x + 3y) / (5t - z) formülünü yazdığınız fonksiyonlarla hesaplatarak ekrana yazın

def fnk_ekrana_yazdir(a):
    print(a)
def fnk_topla(a, b):
    return a + b
def fnk_cikart(a, b):
    return a - b
def fnk_carp(a, b):
    return a * b
def fnk_bol(a, b):
    if b == 0:
        fnk_ekrana_yazdir("Bölümün altı sıfır olamaz")
        return 0
    return a / b
def fnk_convert_str_to_float(str):
    test = ""
    while test == "":
        test = input(str + ":")
    test = float(test)
    return test
fnk_ekrana_yazdir("(2x + 3y) / (5t - z) fonksiyonu için:")
degiskenX = fnk_convert_str_to_float("X")
degiskenY = fnk_convert_str_to_float("Y")
degiskenZ = fnk_convert_str_to_float("Z")
degiskenT = fnk_convert_str_to_float("T")

def denklem_hesapla(x, y, z, t):
    tCarpiBes = fnk_carp(5, t)
    payda = fnk_cikart(tCarpiBes, z)
    if payda == 0:
        fnk_ekrana_yazdir("Payda sıfır olamaz!!")
    else:
        ikiX = fnk_carp(2, x)
        ucY = fnk_carp(3, y)
        pay = fnk_topla(ikiX, ucY)
        sonuc = fnk_bol(pay, payda)
        fnk_ekrana_yazdir( sonuc )
denklem_hesapla(degiskenX, degiskenY, degiskenZ, degiskenT)
