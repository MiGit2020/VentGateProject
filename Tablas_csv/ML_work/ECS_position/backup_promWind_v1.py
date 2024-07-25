#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 02:22:10 2023

@author: pcandia
"""

import pandas as pd

#file1 = open('f_p2_w_1_copy.csv', 'r')
file1 = open('f_p2_w_1.csv', 'r')
lines = file1.readlines()

wd=[]
#lines=['3','-0.1','5','-0.1','-0.1','10']
print("len(lines)):",len(lines))
for i in lines:
        my_list = i.split(',')
#        #my_list = [my_list[-2].strip(),my_list[-1].strip()]
        my_list = my_list[10].strip()
        wd.append(my_list)
wd.pop(0) 
#print('wd: ', wd[0:10])

wf = [float(x) for x in wd]
#print(wf)

j=0
wind=[]
lw=[]
for i in range(len(wf)):
    print("pos i=",i)  
    if wf[i]== 0 :
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
        
        while wf[j]== 0 :
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


