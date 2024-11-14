# Python Programlama 101 Vize Sınavı
**Tarih**: 14.11.2024

### 1) İki sayı arasındaki harmonik ortalamayı hesaplayın.
İki tam sayı arasında harmonik ortalamayı hesaplayan bir fonksiyon yazın. Bu fonksiyon, küçükten büyüğe sırayla tüm sayıları almalı ve harmonik ortalamayı döndürmelidir.

```python
def harmonic_mean(kucuk, buyuk):
    if kucuk > buyuk:
        kucuk, buyuk = buyuk, kucuk  # Değerleri yer değiştir
    sum_of_reciprocals = 0
    count = 0
    
    for num in range(kucuk, buyuk + 1):
        sum_of_reciprocals += 1 / num
        count += 1
    
    if count == 0:
        return 0  
    
    return count / sum_of_reciprocals
```

---

### 2) İki sayı arasındaki asal sayıların sayısını bulun.
Kullanıcıdan alınan iki sayı arasındaki asal sayıların sayısını bulan bir fonksiyon yazın.

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def count_primes_between(kucuk, buyuk):
    if kucuk > buyuk:
        kucuk, buyuk = buyuk, kucuk  # Değerleri yer değiştir
    prime_count = 0
    for num in range(kucuk, buyuk + 1):
        if is_prime(num):
            prime_count += 1
    return prime_count
```

---

### 3) Bir liste içerisindeki en küçük ve en büyük değerlerin ortalamasını hesaplayın.
Bir liste içerisindeki minimum ve maksimum değerlerin ortalamasını bulan bir fonksiyon yazın.

```python
def average_of_min_max(values):
    min_value = values[0]
    max_value = values[0]
    
    for value in values:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
    
    return (min_value + max_value) / 2
```
---

#### 4 ve 5. sorular için aşağıdaki liste oluşturma kodu kullanılmıştır.
```python 
sayi1 = int(input("İlk sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
adet = int(input("Adet sayısını girin: "))

kucuk = sayi2
buyuk = sayi1
if sayi1 < sayi2:
    kucuk = sayi1
    buyuk = sayi2

random_list = []
for _ in range(adet):
    random_list.append(random.randint(kucuk, buyuk))
```

---

### 4) Bir listedeki 3’e bölünebilen sayıların ortalamasını bulun.
Kullanıcıdan alınan iki sayı arasındaki rastgele tam sayılarla dolu bir listeyi kullanarak, 3’e bölünebilen sayıların ortalamasını bulun.

```python
sum_of_divisible = 0
count_of_divisible = 0

for value in random_list:
    if value % 3 == 0:
        sum_of_divisible += value
        count_of_divisible += 1

if count_of_divisible != 0:
    print(sum_of_divisible / count_of_divisible)
```

---

### 5) Kullanıcıdan alınan iki sayı arasında, kullanıcıdan alınan eleman sayısı kadar rastgele elemanlardan oluşan bir liste tanımlayın ve bu listeyi büyükten küçüğe sıralayın.
Kullanıcıdan iki sayı ve bir adet sayısı alın. Bu iki sayı arasında rastgele sayılarla dolu bir liste oluşturun, ardından listeyi büyükten küçüğe sıralayın.

```python
n = len(random_list)
for i in range(n - 1):
    for j in range(i, n):
        if random_list[j] > random_list[j+1]:
            temp = random_list[j]
            random_list[j] = random_list[j+1],
            random_list[j+1] = temp
```
