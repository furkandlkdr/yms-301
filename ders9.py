from operator import index

import pandas as pd
import numpy as np
from pandas import *

#pandas serileri
s=pd.Series(np.arange(5),index=["a","b","c","d","e"])
print(s)

plaka=[1,38,19,55]
il=['Adana','Kayseri','Çorum','Samsun']
il=pd.Series(il,index=plaka)
print(il)
print(il[19])
il[19]='Yeni'
print(il[19])

#dataframe-veri çerçevesi

d={'notu':[20,30,55,65],
   "adi":['Akif','hakan','Ömer','mustafa']}

d=pd.DataFrame(d,columns=['notu','adi'])
print(d)

print(d.iloc[1])
print(d.loc[0])

print(d.loc[[2]])
print(d.loc[3]['adi'])
print(d.iloc[0]['notu'])

print(d.at[1,'notu'])
print(d.iat[2,0])
print(len(d))

print(d.loc[d['notu']>50])

print(d.sample(2))#rastgele örnek almak için kullanılır

d.pop('adi')#sütun silmek için kullanılır
print(d)

veri=pd.read_csv('veri.csv')
print(veri)
print(len(veri))
print(veri.shape)

veri2=pd.read_csv('veri.csv',usecols=['Education Index','Urbanization Rate (%)'])
veri2.rename(columns={'Education Index':'Egitim','Urbanization Rate (%)':'Kentlesme'},inplace=True)

print(veri2.head())
print(veri2.head(20))
