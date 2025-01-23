import numpy as np
import random

from numpy.ma.core import arange, repeat

a = np.arange(5)  # vektör tek boyutlu dizi
boyut = a.ndim
bs = a.shape
print(bs)

a = np.arange(4, 20, 2)
a = np.arange(15)
a = a.reshape(3, 5)
a = a.reshape(5, 3)
b = a.ravel()
print(a)
print(b)
print(a[2][1])

liste = [3, 4, 5, 6, 7, 8, ]
dizi = np.array(liste)
print(liste)
print(dizi)
print(dizi[5])

c = np.arange(24).reshape(2, 3, 4)
print(c)

c1 = np.sum(c, axis=0)
c2 = np.sum(c, axis=1)
c2 = np.sum(c, axis=2)
print(c2)
print("---------------------------------")
# tek boyutlu dizi (vektör) işlemleri
liste = [2, 3, 4]
dizi = np.array(liste)
dizi = np.linspace(0, 5, 3)  # 0-5 arasında 3 adet kesirli sayıdan oluşan dizi
print(dizi)
dizi = np.logspace(0, 2, 3)
print(dizi)
dizi = np.random.rand(4)
print(dizi)
dizi = np.random.randint(1, 9, 5)
print(dizi)
dizi = np.repeat(3, 4)
print(dizi)
dizi = np.zeros(3)
print(dizi)
dizi = np.ones(4)
print(dizi)

dizi = np.array([[2, 3, 4],
                 [5, 6, 7]])
print(dizi)
dizi = np.zeros((2, 3))
print(dizi)
dizi = np.ones((3, 3))
print(dizi)
dizi = np.full((2, 3), 5)
print(dizi)
dizi = np.eye(4)
print(dizi)
dizi = np.random.randint(1, 9, [2, 4])
print(dizi)
dizi = np.random.randn(2, 3)
print(dizi)
dizi = np.random.random((2, 3))
print(dizi)

# kullanıcının girmiş oldugu 2 deger arasında rastgele elemanlardan oluşan
# 2 adet 9 elemanlı listeyi 3X3 matrise çevirerek iki matrsin toplam sonucunu ekrana
# yazdıran programı yazınız

liste1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
liste2 = [3, 4, 5, 6, 3, 2, 3, 8, 7]

liste1 = np.array(liste1)
liste2 = np.array(liste2)
a = liste1.reshape(3, 3)
b = liste2.reshape(3, 3)
print(a)
print(b)
tpl = np.add(a, b)  # matris toplama işlemi gerçekleştirir
snc = np.matmul(a, b)  # matris çarpımı gerçekleştirir
print(snc)
