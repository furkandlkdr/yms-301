import random

##Soru1
def harmonic_mean(kucuk, buyuk):
    if kucuk > buyuk:
        kucuk, buyuk = buyuk, kucuk # Swap the values

    sum_of_reciprocals = 0
    count = 0
    
    for num in range(kucuk, buyuk + 1):
        sum_of_reciprocals += 1 / num
        count += 1
    
    if count == 0:
        return 0  
    
    return count / sum_of_reciprocals

##Soru 2
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def count_primes_between(kucuk, buyuk):
    if kucuk > buyuk:
        kucuk, buyuk = buyuk, kucuk # Swap the values
    
    prime_count = 0
    for num in range(kucuk, buyuk + 1):
        if is_prime(num):
            prime_count += 1
    
    return prime_count

##Soru 3
def average_of_min_max(values):
    min_value = values[0]
    max_value = values[0]
    
    for value in values:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
    
    return (min_value + max_value) / 2

## Soru 4 ve 5 için liste
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

## Soru 4
sum_of_divisible = 0
count_of_divisible = 0

for value in random_list:
    if value % 3 == 0:
        sum_of_divisible += value
        count_of_divisible += 1

if count_of_divisible != 0:
    print(sum_of_divisible / count_of_divisible)

## Soru 5
n = len(random_list)
for i in range(n - 1):
    for j in range(i, n):
        if random_list[j] > random_list[j+1]:
            temp = random_list[j]
            random_list[j] = random_list[j+1],
            random_list[j+1] = temp
