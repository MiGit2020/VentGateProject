#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 17:19:08 2023

@author: pcandia
"""

from datetime import datetime, timedelta
import csv
#import pandas as pd
import os
import sys

os.remove('f_p2_w_1_fin2.txt')
os.system('touch f_p2_w_1_fin2.txt')


def convertir_fecha_decimal(numero):
    # Convertir la fecha decimal en un objeto datetime
    fecha_base = datetime(1899, 12, 30)
    delta = timedelta(days=numero)
    fecha = fecha_base + delta

    # Formatear la fecha en un formato legible
    fecha_formateada = fecha.strftime("%m/%d/%Y")
    print('numero:',numero)
    #p_entera=int(numero)
    p_decimal= numero % 1
    hora= int(p_decimal*24)
    hora2 = format(hora, '02')
    min= int(((p_decimal*24) % 1)*60)
    min2 = format(min, '02')
    seg= int(((((p_decimal*24) % 1)*60) % 1)  *60)
    seg2= format(seg, '02') 
    #if fecha== -0.1:
        #return(fila[0],fila[1],fila[7],fila[9])

    #print("--> ",fila)
    f=open("f_p2_w_1_fin2.txt", "a")
    linea=fecha_formateada+',  '+hora2+':'+min2+':'+seg2+',  '+ format(float(fila[1]),'.5f') + ',  '+ format(float(fila[2]),'.1f')+',  '+ format(float(fila[3]),'.1f') +',  '+format(float(fila[4]),'.1f') +',  '+ str(fila[5]) +',  '+ str(fila[6]) + ',  '+format(float(fila[7]),'.1f') +',  '+ format(float(fila[9]),'.1f') + '\n'
    #linea=fecha_formateada+' '+hora2+':'+min2 +' '+ format(float(fila[1]),'.5f')+' '+ format(float(fila[2]),'.1f') +' '+ format(float(fila[3]),'.1f') +' '+format(float(fila[4]),'.1f') +' '+format(float(fila[5]),'.1f') +' ' +format(float(fila[6]),'.1f') +' '+fila[8]+ ' ' +fila[10] + '\n'
    f.write(linea)
    f.close()
    
 
with open('f_p2_w_1_fin1.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        if fila[0]=='fecha' or fila[1] == 'datetime' or fila[2]=='ecs_az_pos' or fila[3]=='topshut_pos' or fila[4]=='botshut_pos' or fila[5]=='eastVent_pos' or fila[6]=='westVent_pos' or fila[7]=='pwfs2_see' or fila[9]=='windAve':
            pass
        #elif fila[0]== '-0.1' and fila[7]=='-0.1':
            #print('fila 0,7: ',fila[0],fila[7])
        else:
            numero = float(fila[1])
            fecha_legible = convertir_fecha_decimal(numero)
            print(fecha_legible)
            