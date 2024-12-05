# Sayısal işlemlere giriş yapıyoruz, bazı sınıfları öğreneceğiz.
# İlk öğreneceğimiz sınıf İstatistik, (statistics)
from statistics import *

liste = [2, 4, 6, 8, 11, 15, 19]
liste2 = [2, 4, 6, 8.4, 11.5, 15, 19, 100]

# Mean fonksiyonu yalnızca tüm elemanları tam sayı olan listelerde çalışır.
ort = mean(liste)
# Float içeren bir listenin ort hesaplamak için fmean kullanıyoruz.
ort = fmean(liste2)
# geometrik ort. kullanarak verilerimizin içerisindeki homojen ortalamayı buluyoruz
# sıfır veya eksi içeren verilerde kullanılamaz
ort = geometric_mean(liste)
# Harmonik ort. uç değerlerin etkisini azaltmak amaçlı ortaya çıkmış.
ort = harmonic_mean(liste)
print(ort)

# Medyan; küçükten büyüğe sıralanmış bir dizideki ortanca elemanı getirir. Yoksa ortadakilerin ortalamasını getirir.
medyan = median(liste)
# median_low(liste) median_high(liste) işlemleri iki ortancadan küçük veya büyük olanı getirir.
print(medyan)

# Çeyrekler (Quantiller)
# 4 parçaya bölmek için hangi noktalardan bölünmesi gerektiğini söylüyor
ceyrekler = quantiles(liste)
# Kaça ayırmak istiyorsak n yerine onu yazıyoruz, o bizim için ayrım noktalarını söylüyor.
# Burayı büyüttükçe her veri arasında o aralığı eşit bölecek şekilde aralık belirliyor.
ceyrekler = quantiles(liste, n=5)
print(ceyrekler)

# Mod (Tepedeğer)
# Bir veri topluluğunda en sık görülen değerdir.
# Sıklıkları eşitse ilk olarak gördüğünü getirir
liste3 = [1, 1, 2, 3, 4, 3, 5, 1, 2, 2]
tekrar = mode(liste3)
# Multimode fonksiyonu ile sıklıkları eşit olan tüm değerleri getirir.
tekrar = multimode(liste3)
print(tekrar)

# Varyans
# Örneklem ve kitle varyansı ayrı şeylerdir. Örneklemde eleman sayımıza göre davranırken,
# kitlede genele göre davranırız. Koddaki tek fark birinde n-1'e diğerinde n'e bölmemizdir.
varyans = variance(liste)  # Örneklem varyansı
kitle_varyans = pvariance(liste)  # Kitle varyansı
print(varyans)
print(kitle_varyans)

# Standart Sapma
# Varyansın kareköküdür.
ss = stdev(liste)  # Örneklem ss.
ss_kitle = pstdev(liste)  # Kitle ss.
print(ss)
print(ss_kitle)

# Kovaryans
# İki değişkenin birlikte ne kadar değiştiklerinin ölçüsüdür. Listelerin boyu aynı olmalı.
x = [2, 3, 4, 6, 8, 9]
y = [1, 3, 5, 6, 7, 8]
kv = covariance(x, y)
print(kv)

# Korelasyon
# İki değişken arasındaki doğrusal ilişkinin yönünü ve gücünü belirtir.
kk = correlation(x, y)
print(kk)

# Regresyon analizi
# İki ya da daha çok nicel değişken arasındaki ilişkiyi ölçmek için kullanılan analiz metodudur.
# y = a + bx
yil = [2020, 2021, 2022, 2023, 2024]
satis = [100, 210, 360, 400, 510]
b, a = linear_regression(yil, satis)
print('a:', a)
print('b:', b)
y = a + b * 2030
print('y:', y)
