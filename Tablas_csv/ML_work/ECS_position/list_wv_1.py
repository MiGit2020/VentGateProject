#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:58:56 2023
Completar celdas de weast ventgate sin valores, de tal manera que exista un valor para P2.
@author: pcandia
"""


import pandas as pd

#lines=[2,  -0.1,  -0.1,  4,  4,  -0.1,  -0.1,  6,  6,  6,  -0.1,  -0.1 ]
#tp= [44568.23264,44568.23284,44568.23319,44568.23333,44568.23354,44568.23389,44568.23403,44568.23424,44568.23472,44568.23502,44568.23537,44568.23542]

wv=[]
dtime=[]

#for i in lines:
        #my_list = i.split(',')
#        ev.append(i)

#for i in tp:
#    dtime.append(i)

file1 = open('list_wv_1.csv', 'r')
lines = file1.readlines()     
for i in lines:
        my_list = i.split(',')
        my_list1 = my_list[1].strip()
        my_list2 = my_list[2].strip()
        dtime.append(my_list1)
        wv.append(my_list2)        

wv.pop(0)  #eliminamos primer elemento,texto east ventgate
dtime.pop(0) #eliminamos primer elemento,texto datetime


wf = [float(x) for x in wv] #convertir string a float.
dtime2 = [format(float(s),'.5f') for s in dtime] #convertir string a float


j=0
wvp=[]
fch=[]
diff=[]
lw=[]
for i in range(len(wf)):
    print("pos i=",i)  
    if wf[i]== -0.1 :
        wvp.append(prom)
        fch.append(dtime[i])
    if wf[i] >= 0:
        wvp.append(wf[i])
        fch.append(dtime[i])
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
                if wf[j] >=0:
                    dif=(float(dtime[j])-float(dtime[i]))*24*60
                    if dif < 1.2:
                        V2= wf[j]
                        print("i,j:", i,j)
                        print("dif: ",dif)
                        print("V2: ",wf[j])
                        print("V1,V2: ", V1,V2)
                        prom=format((V1+V2)/2, '.1f')
                        print("promedio=",prom)
                    else:
                        prom= -0.1
                    
                        
                                          
print("evp= ",wvp)
print('len(wvp): ', len(wvp))
print("len(wf): ", len(wf))
print("wf[-1]: ", wf[-1])

d = {'Datetime':dtime2, 'westV_fill':wvp}
rf = pd.DataFrame(d)
print(rf.head(20))
rf.to_csv('list_wv_2.csv', index=False)
