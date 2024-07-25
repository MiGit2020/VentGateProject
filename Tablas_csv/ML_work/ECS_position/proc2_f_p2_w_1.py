#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 01:15:36 2023
Este script promedia seeing de P2 y como los valores de viento ya son promedios
de 5min, copio el ultimo
@author: pcandia
"""

import pandas as pd

#file1 = open('test_f_p2_w_2.csv', 'r')
file1 = open('proc2_f_p2_w_2_fin3.csv', 'r')
lines = file1.readlines()


tb=[]
#lines=['3','-0.1','5','-0.1','-0.1','10']
#print("len(lines)):",len(lines))

for i in lines:
        my_list = i.split(',')
        my_wd = my_list[10].strip()
        my_p2 = my_list[9].strip()
        my_dt = my_list[3].strip()
        tb.append((my_dt,my_p2,my_wd))


#print('tabla: ',tb)
print('len(tb1)', len(tb))


j=0
nt=[]
npv=[]

for i in range(len(tb)):
    print("pos i=",i)  
    if float(tb[i][2])== -0.1:
        nt.append((tb[i][0],tb[i][1],V2))
    if float(tb[i][2]) > 0:
        nt.append((tb[i][0],tb[i][1],tb[i][2]))
        print("V1: ",tb[i][2])
        V1=tb[i][2]
        if (len(tb)-1)== j:
            break
        j=i+1
        print("j1= ",j)
        print("tb[j][2]:",tb[j][2])
        print('index= :',tb.index(tb[-1]))
        pv=[]
        k=0
        sum=0
        while float(tb[j][2])== -0.1 :
                if float(tb[j][1]) > 0:
                    pv.append((tb[j][1]))
                    sum=sum+float(tb[j][1])
                    print('p2=',tb[j][1])
                    k=k+1
                #ave=sum/k
                #print('p2=',tb[j][1])
                print('k-->',k)
                j=j+1
                print("j2=",j)
                if float(tb[j][2]) >0:
                    if k>0:
                        ave=sum/k
                    if k==0:
                        ave=0
                    print('ave=',ave)
                    npv.append((tb[j][0],format(ave,'.2f'),tb[j][2]))
                    V2= tb[j][2]
                    print("V2: ",tb[j][2])
                    print("V1,V2: ", V1,V2)
                                                            
print('npv=',npv)
print("len(tb): ", len(tb))
print("tb[-1]: ", tb[-1])


#print('nt= ',nt)
aa=[]
bb=[]
cc=[]
#for k in range(len(nt)):
#    aa.append(nt[k][0])
#    bb.append(nt[k][1])
#    cc.append(nt[k][2])
#print('len(aa)=',len(aa))
#print('len(bb)=',len(bb))
#print('len(cc)=',len(cc))
#d = {'datetime':aa, 'p2':bb, 'wind':cc}
#rf = pd.DataFrame(d)
#print(rf.tail)

print('len(npv)',len(npv))
pa=[]
pb=[]
pc=[]
for k in range(len(npv)):
    pa.append(npv[k][0])
    pb.append(npv[k][1])
    pc.append(npv[k][2])
    
da= {'datetime':pa, 'p2':pb, 'wind':pc}
rda = pd.DataFrame(da)
#print(rda.head(10))
rda.to_csv('test_proc2_f_p2_w_2_out.csv', index=False)

