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

Bir veri kümesinde bağımsız değişken (X) ve bağımlı değişken (Y) değerleri verilmiştir. X = \[1, 2, 3, 4, 5\], Y = \[2, 4, 5, 4, 5\]. Bu verileri kullanarak bir lineer regresyon modeli oluşturun ve tahmin edilen Y değerlerini yazdırın.

#### Cevap:

```Python
import numpy as np

# Veriler
X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 4, 5, 4, 5])

# Ortalama hesaplama
mean_X = np.mean(X)
mean_Y = np.mean(Y)

# Eğim (b) hesaplama
b = np.sum((X - mean_X) * (Y - mean_Y)) / np.sum((X - mean_X) ** 2)

# Kesim noktası (a) hesaplama
a = mean_Y - b * mean_X

# Tahmin edilen Y değerleri
predicted_Y = a + b * X

print("Orijinal Y değerleri:", Y)
print("Tahmin edilen Y değerleri:", predicted_Y)
print("Eğim (b):", b)
print("Kesişim noktası (a):", a)

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

# Rastgele liste oluştur ve matrise çevir
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
import numpy as np

# Dosyayı oku
df = pd.read_csv("Bilgi.csv")

# 'incidence rate' sütununu al ve 'GorOr' ismiyle yeniden adlandır
df['GorOr'] = df['incidence rate']

# İlk 20 veriyi al
data = df['GorOr'].head(20)

# Standart sapmayı hesapla
std_dev = np.std(data)

print("İlk 20 verinin standart sapması:", std_dev)

```
