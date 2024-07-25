#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 17:14:40 2023

@author: pcandia
"""

import pandas as pd

#lines=[2,  -0.1,  -0.1,  4,  4,  -0.1,  -0.1,  6,  6,  6,  -0.1,  -0.1 ]
#tp= [44568.23264,44568.23284,44568.23319,44568.23333,44568.23354,44568.23389,44568.23403,44568.23424,44568.23472,44568.23502,44568.23537,44568.23542]

ev=[]
dtime=[]

#for i in lines:
        #my_list = i.split(',')
#        ev.append(i)

#for i in tp:
#    dtime.append(i)

file1 = open('list_az_1.csv', 'r')
lines = file1.readlines()     
for i in lines:
        my_list = i.split(',')
        my_list1 = my_list[1].strip()
        my_list2 = my_list[2].strip()
        dtime.append(my_list1)
        ev.append(my_list2) 

#print(ev)

ev.pop(0)  #eliminamos primer elemento,texto east ventgate
dtime.pop(0) #eliminamos primer elemento,texto datetime


wf = [float(x) for x in ev] #convertir string a float.
dtime2 = [format(float(s),'.5f') for s in dtime] #convertir string a float

print(wf[-1])
print('indice= :',wf.index(wf[-1]))

j=0
evp=[]
fch=[]
diff=[]
lw=[]
for i in range(len(wf)):
    #print("pos i=",i)  
    if wf[i]== -0.1 :
        evp.append(prom)
        fch.append(dtime[i])
    if wf[i] >= 0:
        evp.append(wf[i])
        fch.append(dtime[i])
        #print("V1: ",wf[i])
        V1=wf[i]
        #if wf.index(wf[-1])== j:
         #   break
        if (len(wf)-1)== j:
            break
        j=i+1
        #print("j1= ",j)
        #print("wf[j1]:",wf[j])
        #print('index= :',wf.index(wf[-1]))
        #print('last value= :',wf[-1])
        
        while wf[j]== -0.1 :
                j=j+1
                #print("j2=",j)
                #print("wf[j2]: ", wf[j])
                try:
                    if wf[j] >=0:
                        dif=(float(dtime[j])-float(dtime[i]))*24*60
                        if dif < 1.2:
                            V2= wf[j]
                            #print("i,j:", i,j)
                            #print("dif: ",dif)
                            #print("V2: ",wf[j])
                            #print("V1,V2: ", V1,V2)
                            prom=format((V1+V2)/2, '.1f')
                            #print("promedio=",prom)
                        else:
                            prom= -0.1
                except Exception as e:
                    print("An error occurred:", str(e))
                    
                        
                                          
print("evp= ",evp)
#print('datetime: ', dtime2)
print('len(evp): ', len(evp))
print("len(datetime): ", len(dtime2))
print("az[-1]: ", wf[-1])
print("datetime[-1]: ", dtime2[-1])

d = {'Datetime':dtime2, 'az_fill':evp}
rf = pd.DataFrame(d)
print(rf.head(20))
rf.to_csv('list_az_2.csv', index=False)
