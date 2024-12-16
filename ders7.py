from statistics import *

liste=[2,4,6,8,11,15,19,21]
#aritmetik ortalama
ort=mean(liste)
ort2=fmean(liste)

#geometrik ortalama
ort=geometric_mean(liste)

#harmonik ortlama
ort=harmonic_mean(liste)

#medyan
medyan=median(liste)
medyan=median_low(liste)
medyan=median_high(liste)
medyan=median_grouped(liste)

#çeyrekler
ceyrekler=quantiles(liste)
ceyrekler2=quantiles(liste,n=20)
#print(ceyrekler)
#print(ceyrekler2)

#mod
liste2=[2 ,1 ,1,2,2, 3, 4, 3, 5, 1]
tekrar=mode(liste2)
tekrar=multimode(liste2)

#varyans
varyans=variance(liste)#örneklem varyansını hesaplar
kitle_varyansi=pvariance(liste)#kitle varyansını hesaplar

#standart sapma
ss=stdev(liste)#örneklemin standart sapması
ss_kitle=pstdev(liste)#kitle standart sapması

#kovaryans
x=[2,3,4,6,8,9]
y=[1,3,5,6,7,8]
kv=covariance(x,y)

#korelasyon katsayısı
kk=correlation(x,y)


#regresyon analizi
yil=[2020,2021,2022,2023,2024]
satis=[100,210,360,400,510]
b,a=linear_regression(yil,satis)
#y=a+bx
print("a:",a)
print("b",b)
y=a+b*2025
print(y)

# kullanıcını girmiş olduğu degerler arasında yine kullanıcının
#girmiş olduğu deger kadar oluşan bir listede
#görmüş olduğumuz istatistiki bilgileri yazdırınız
