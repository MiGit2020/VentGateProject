#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 02:52:01 2023
calcula promedios de viento
@author: pcandia
"""

import pandas as pd

wsp=['2','0','0','4.24','0','0','0','6','0','0','0','8']
wsp2= ['1','2','3','4','5','6','7','8','9','10','11','12']

#wd=['3','7']
wd = [float(x) for x in wsp]

print(wd)

j=0
wind=[]
lw=[]
for i in range(len(wd)):
    print("pos i=",i)  
    if wd[i]== 0 :
        wind.append(prom)
    if wd[i] > 0:
        wind.append(wd[i])
        print("V1: ",wd[i])
        V1=wd[i]
        #if wd.index(wd[-1])== j:
        #    break
        if len(wd)-1 ==j:
            break
        j=i+1
        print("j1= ",j)
        print("wd[j1]:",wd[j])
        print('index= :',wd.index(wd[-1]))
        
        while wd[j]== 0 :
                j=j+1
                print("j2=",j)
                if wd[j] >0:
                    V2= wd[j]
                    print("V2: ",wd[j])
                    print("V1,V2: ", V1,V2)
                    prom=format((V1+V2)/2, '.1f')
                    print("promedio=",prom)
                    
                        
                                          
print("wind= ",wind)
print("lenwind: ",len(wd))
print("index:",wsp.index('8'))


df = pd.DataFrame(wind)
file_path = 'test3_out1.csv'
df.to_csv(file_path, index=False)
td1 = pd.read_csv('test3_out1.csv')
td1['windCol'] = td1['0'].astype(str) 
print(td1.head(12))
td2= td1.rename(columns= {'0':'windAve'}, inplace = False)
print(td2.head(12))
df = td2.drop('windCol', axis=1)
print(df.head(12))







   
