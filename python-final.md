### 1) Kullanıcının girdiği sayıya kadar Fibonacci dizisinin elemanlarını toplayıp ortalamasını alan ve yazdıran kod

#### Soru:

Kullanıcının girdiği sayıya kadar Fibonacci dizisinin elemanlarını toplayıp ortalamasını hesaplayan bir Python programı yazınız. (Fibonacci dizisi: 1, 1, 2, 3, 5, 8...)

#### Cevap:

```Python
def fibonacci_average(limit):
    a, b = 1, 1
    fibonacci = [a]
    while b <= limit:
        fibonacci.append(b)
        a, b = b, a + b
    total = sum(fibonacci)
    average = total / len(fibonacci)
    return fibonacci, total, average

limit = int(input("Bir sayı giriniz: "))
fibonacci, total, average = fibonacci_average(limit)
print("Fibonacci dizisi:", fibonacci)
print("Toplam:", total)
print("Ortalama:", average)

```

___

### 2) Lineer regresyon analizi içeren bir soru

#### Soru:

2021, 2022, 2023 ve 2024 yıllarına ait satış verileri verilmiştir. Bu verileri kullanarak bir lineer regresyon modeli oluşturun ve 2025 yılı için tahmin edilen satış değerini yazdırın.

#### Cevap:

```Python
from statistics import *

yil = [2021, 2022, 2023, 2024]
satis = [1000, 1500, 1752, 1900]

b, a = linear_regression(yil, satis)
y = a + b * 2025

print(a)
print(b)
print("2025 tahmini: ", y)
```

___

### 3) Rastgele elemanlardan oluşan bir liste oluşturup matrise çevirme ve düzenleme

#### Soru:

Kullanıcıdan alt ve üst sınır alarak, bu aralıkta rastgele elemanlardan oluşan 9 elemanlı bir liste oluşturun. Bu listeyi 3x3 bir matrise çevirin. Matriste, 1. satır 1. sütunda en küçük eleman, 3. satır 3. sütunda en büyük eleman olacak şekilde düzenleme yapınız.

#### Cevap:

```Python
import numpy as np

# Kullanıcıdan alt ve üst sınır al
alt_sinir = int(input("Alt sınır: "))
ust_sinir = int(input("Üst sınır: "))

# Rastgele liste oluştur ve matrise çevir. NP ile oluşturulduğundan vektör olarak alınır. Tekrar dönüştürme gerektirmez
liste = np.random.randint(alt_sinir, ust_sinir + 1, 9)
matris = liste.reshape(3, 3)

# Listeyi en küçükten en büyüğe sıralama (manuel)
for i in range(len(liste)):
    for j in range(i + 1, len(liste)):
        if liste[i] > liste[j]:
            liste[i], liste[j] = liste[j], liste[i]

# Sıralanmış listeyi matrise çevirme
matris_siralanmis = liste.reshape(3, 3)

print("Orijinal 3x3 Matris:")
print(matris)
print("Sıralanmış 3x3 Matris:")
print(matris_siralanmis)


```

___

### 4) CSV dosyasından veri okuma ve standart sapma hesaplama

#### Soru:

**Bilgi.csv** adlı dosyada **incidence rate** sütununda bulunan verilerden ilk 20 tanesini alın. Bu verilerin standart sapmasını hesaplayın ve sonucu yazdırın. Sütunu 'GorOr' ismiyle işleyin.

#### Cevap:

```Python
import pandas as pd

# Dosyayı oku
df = pd.read_csv("Bilgi.csv")

# 'incidence rate' sütununu al ve 'GorOr' ismiyle yeniden adlandır
df.rename(columns={'incidence rate':'GorOr'},inplace=True)

# İlk 20 veriyi al
data = df['GorOr'].head(20)

# Ortalama hesapla
mean = 0
for value in data:
    mean += value
mean /= len(data)

# Varyans hesapla
variance = 0
for value in data:
    variance += (value - mean) ** 2
variance /= len(data)

# Standart sapma hesapla
std_dev = variance ** 0.5

print("İlk 20 verinin standart sapması:", std_dev)

```
