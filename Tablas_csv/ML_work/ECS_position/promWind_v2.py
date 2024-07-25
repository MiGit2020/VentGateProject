#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 01:17:51 2023

@author: pcandia
"""

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

wd0=[]
wd1=[]
wd2=[]
wd3=[]
wd4=[]
wd5=[]
wd6=[]
wd8=[]
wd10=[]

#lines=['3','-0.1','5','-0.1','-0.1','10']
print("len(lines)):",len(lines))
for i in lines:
        my_list = i.split(',')
        my_list0 = my_list[0].strip() #fecha_x
        my_list1 = my_list[1].strip() #datetime
        my_list2 = my_list[2].strip() #ecs_az_pos
        my_list3 = my_list[3].strip() #topshut_pos
        my_list4 = my_list[4].strip() #botshut_pos
        my_list5 = my_list[5].strip() #eastVent_pos
        my_list6 = my_list[6].strip() #westVent_pos
        #my_list7 = my_list[7].strip() #fecha_y
        my_list8 = my_list[8].strip() #pwfs2_see
        #my_list9 = my_list[9].strip()  #fecha
        my_list10 = my_list[10].strip() #windSp
        wd0.append(my_list0)
        wd1.append(my_list1)
        wd2.append(my_list2)
        wd3.append(my_list3)
        wd4.append(my_list4)
        wd5.append(my_list5)
        wd6.append(my_list6)
        #wd7.append(my_list7)
        wd8.append(my_list8)
        #wd9.append(my_list9)
        wd10.append(my_list10)
        
        
wd0.pop(0),wd1.pop(0),wd2.pop(0),wd3.pop(0),wd4.pop(0),wd5.pop(0),wd6.pop(0),wd8.pop(0),wd10.pop(0)


wf0 = [x for x in wd0] #fecha_x
wf1 = [float(x) for x in wd1]
wf2 = [x for x in wd2]
wf3 = [x for x in wd3]
wf4 = [x for x in wd4]
wf5 = [x for x in wd5]
wf6 = [x for x in wd6]
#wf7 = [x for x in wd7] #fecha_y
wf8 = [float(x) for x in wd8]
#wf9 = [x for x in wd9]  #fecha
wf10 = [float(x) for x in wd10]


j=0
wind=[]
lw=[]
for i in range(len(wf10)):
    print("pos i=",i)  
    if wf10[i]== -0.1 :
        wind.append(prom)
    if wf10[i] > 0:
        wind.append(wf10[i])
        print("V1: ",wf10[i])
        V1=wf10[i]
        #if wf.index(wf[-1])== j:
         #   break
        if (len(wf10)-1)== j:
            break
        j=i+1
        print("j1= ",j)
        print("wd[j1]:",wf10[j])
        print('index= :',wf10.index(wf10[-1]))
        
        while wf10[j]== -0.1 :
                j=j+1
                print("j2=",j)
                if wf10[j] >0:
                    V2= wf10[j]
                    print("V2: ",wf10[j])
                    print("V1,V2: ", V1,V2)
                    prom=format((V1+V2)/2, '.1f')
                    print("promedio=",prom)
                    
                        
                                          
print("wind= ",wind)
print('len(wind): ', len(wind))
print("len(wf): ", len(wf10))
#print("wf[-1]: ", wf[-1])

#df = pd.DataFrame(wind)
#df.to_csv('promW_out1.csv', index=False)
#td1 = pd.read_csv('promW_out1.csv')

#td1['windCol'] = td1['0'].astype(str) 
#print(td1.head(20))
#td2= td1.rename(columns= {'0':'windAve'}, inplace = False)
#print(td2.head(30))

#df = td2.drop('windCol', axis=1)
#print(df.head(5))
#df.to_csv('f_p2_w_1_copy_out.csv', index=False)


#dtime2_1 = pd.DataFrame(dtime2)
#print(dtime2_1.head(10))

d = {'fecha':wf0,'datetime':wf1,'ecs_az_pos':wf2,'topshut_pos':wf3,'botshut_pos':wf4,'eastVent_pos':wf5,'westVent_pos':wf6,'pwfs2_see':wf8,'windSp':wf10, 'windAve':wind}
rf = pd.DataFrame(d)
print(rf.head(10))
rf.to_csv('f_p2_w_1_copy_out2.csv', index=False)

