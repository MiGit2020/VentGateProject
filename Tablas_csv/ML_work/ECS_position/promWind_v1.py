#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 00:08:28 2023

Calcular promedios de viento.

@author: pcandia
"""
#import numpy as np
import pandas as pd

#file1 = open('f_p2_w_1_copy.csv', 'r')
file1 = open('f_p2_w_1.csv', 'r')
lines = file1.readlines()

wd=[]
dtime=[]
#lines=['3','-0.1','5','-0.1','-0.1','10']
#print("len(lines)):",len(lines))

for i in lines:
        my_list = i.split(',')
        my_list1 = my_list[10].strip()
        my_list2 = my_list[1].strip()
        wd.append(my_list1)
        dtime.append(my_list2)
        
wd.pop(0)  #eliminamos primer elemento,texto winSp
dtime.pop(0) #eliminamos primer elemento,texto datetime
#print('wd: ', wd[0:10])

wf = [float(x) for x in wd] #convertir string a float.
#dtime2 = [format(float(s),'.5f') for s in dtime] #convertir string a float
dtime2 = [float(s) for s in dtime] #convertir string a float

j=0
wind=[]
lw=[]
for i in range(len(wf)):
    print("pos i=",i)  
    if wf[i]== -0.1 :
        wind.append(prom)
    if wf[i] > 0:
        wind.append(wf[i])
        print("V1: ",wf[i])
        V1=wf[i]
        #if wf.index(wf[-1])== j:
         #   break
        if (len(wf)-1)== j:
            break
        j=i+1
        print("j1= ",j)
        print("wd[j1]:",wf[j])
        print('index= :',wf.index(wf[-1]))
        
        while wf[j]== -0.1 :
                j=j+1
                print("j2=",j)
                if wf[j] >0:
                    V2= wf[j]
                    print("V2: ",wf[j])
                    print("V1,V2: ", V1,V2)
                    prom=format((V1+V2)/2, '.1f')
                    print("promedio=",prom)
                    
                        
                                          
print("wind= ",wind)
print('len(wind): ', len(wind))
print("len(wf): ", len(wf))
print("wf[-1]: ", wf[-1])

#df = pd.DataFrame(wind)
#df.to_csv('promW_out1.csv', index=False)
#td1 = pd.read_csv('promW_out1.csv')

#td1['windCol'] = td1['0'].astype(str) 
#print(td1.head(20))
#td2= td1.rename(columns= {'0':'windAve'}, inplace = False)
#print(td2.head(30))
#df = td2.drop('windCol', axis=1)
#print(df.head(20))
#df.to_csv('f_p2_w_1_copy_out.csv', index=False)


d = {'datetime':dtime2, 'wind':wind}
rf = pd.DataFrame(d)
print(rf.head(10))
rf.to_csv('f_p2_w_1_out.csv', index=False)

print('len_wd2:',len(dtime2))
print('len_dtime:',len(dtime2))
