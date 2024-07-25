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
file1 = open('tabla2_fin1.csv', 'r')

lines = file1.readlines()



with open('test_fin2.csv', 'r') as file:
    for i in range(3):
        line = file.readline()
        if not line:
            break
        print(line.strip())  # Remove leading/trailing whitespace if needed



tb=[]
#lines=['3','-0.1','5','-0.1','-0.1','10']
#print("len(lines)):",len(lines))

for i in lines:
        my_list = i.split(',')
        fech = my_list[0].strip()
        hr = my_list[1].strip()
        dt = my_list[2].strip()
        azp= my_list[3].strip()
        topshut = my_list[4].strip()
        botshut = my_list[5].strip()
        event = my_list[6].strip()
        wvent = my_list[7].strip()
        p2 = my_list[8].strip()
        wd = my_list[9].strip()
        print('wd:',wd)
        wdir = my_list[10].strip()
        tb.append((fech,hr,dt,azp,topshut,botshut,event,wvent,p2,wd,wdir))


#tb.pop(0)
print('len(tb1)', len(tb))
print('tb: ', tb)

#tb[0] fecha, tb[1] hour, tb[2] datetime, tb[3] az tel, tb[4] top shutter
#tb[5] bot shutter, tb[6] east Vent., tb[7] west Vent., tb[8] p2, tb[9] wins sp., tb[10] wind dir.

j=0
nt=[]
npv=[]

for i in range(len(tb)):
    print("pos i=",i)  
    if float(tb[i][2])== -0.1:
        #nt.append((tb[i][0],tb[i][1],tb[i][2],tb[i][3],tb[i][4],tb[i][5],tb[i][6],tb[i][7],tb[i][8],V2,tb[i][10]))
        pass
    if float(tb[i][2]) > 0:
        #nt.append((tb[i][0],tb[i][1],tb[i][2],tb[i][3],tb[i][4],tb[i][5],tb[i][6],tb[i][7],tb[i][8],tb[i][9],tb[i][10]))
        print("V1: ",tb[i][9])
        V1=tb[i][9]
        if (len(tb)-1)== j:
            break
        j=i+1
        print("j1= ",j)
        print("tb[j][9]:",tb[j][9])
        print('index= :',tb.index(tb[-1]))
        pv=[]
        k=0
        sum=0
        while float(tb[j][9])== -0.1 :
                if float(tb[j][9]) > 0:
                    pv.append((tb[j][8]))
                    sum=sum+float(tb[j][8])
                    print('p2=',tb[j][8])
                    k=k+1
                #ave=sum/k
                #print('p2=',tb[j][1])
                print('k-->',k)
                j=j+1
                print("j2=",j)
                if float(tb[j][9]) >0:
                    if k>0:
                        ave=sum/k
                    if k==0:
                        ave=0
                    print('ave=',ave)
                    npv.append((tb[i][0],tb[i][1],tb[i][2],tb[i][3],tb[i][4],tb[i][5],tb[i][6],tb[i][7],format(ave,'.2f'),tb[j][9],tb[j][10]))
                    V2= tb[j][9]
                    print("V2: ",tb[j][9])
                    print("V1,V2: ", V1,V2)
                                                            
print('npv=',npv)
print("len(tb): ", len(tb))
print("tb[-1]: ", tb[-1])


print('len(npv)',len(npv))
fa=[] #fecha
fb=[] #hora
fc=[] #datetime
fd=[] #Tel. azimuth
fe=[] #top shutter
ff=[] #bot. Shutter
fg=[] #east ventgate
fh=[] #west ventgate
fi=[] #p2
fj=[] #wind speed
fk=[] # wind dir
for k in range(len(npv)):
    fa.append(npv[k][0])
    fb.append(npv[k][1])
    fc.append(npv[k][2])
    fd.append(npv[k][3])
    fe.append(npv[k][4])
    ff.append(npv[k][5])
    fg.append(npv[k][6])
    fh.append(npv[k][7])
    fi.append(npv[k][8])
    fj.append(npv[k][9])
    fk.append(npv[k][10])   
da= {'fecha':fa, 'hora':fb, 'datetime':fc, 'az_pos':fd, 'top_shutter':fe, 'bot. Shutter':ff, 'eastVent_pos':fg, 'westVent_pos':fh, 'p2':fi, 'wind':fj,'windDir':fk}
rda = pd.DataFrame(da)
#print(rda.head(10))
rda.to_csv('tabla3.csv', index=False)

