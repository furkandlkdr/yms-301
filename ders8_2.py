import numpy as np
import random

# kullanıcının girmiş olduğu degerler arasında rastgele 9 elemandan oluşan bir liste
#oluşturunuz bu listeyi 3X3 matrise çevirerek yazdırınız

d1=int(input("1. deger :"))
d2=int(input("2. deger "))
liste=[]

for i in range(9):
    rs=random.randint(d1,(d2+1))
    liste.append(rs)

print(liste)
dizimiz=np.array(liste)
matris=dizimiz.reshape(3,3)
print(matris)
tpl=0
eb=matris[0][0]
for i in range(3):
    for j in range(3):
        tpl=tpl+matris[i][j]
        if eb<matris[i][j]:
            eb=matris[i][j]
print("toplam",tpl)
print("En büyük",eb)
