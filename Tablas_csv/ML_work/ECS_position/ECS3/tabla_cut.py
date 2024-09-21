#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 22:04:02 2024

@author: pcandia
"""

from datetime import datetime, timedelta
import csv

def cutcolum(fila,numero):

    fecha_base = datetime(1899, 12, 30)
    #print('fecha_base:',fecha_base)
    delta = timedelta(days=numero)
    #print('delta:', delta)
    fecha = fecha_base + delta
    #print('fecha=',fecha)
    hms = fecha.strftime("%H:%M:%S")
    #print("hms:", hms)
    fecha_formateada = fecha.strftime("%m/%d/%Y")
    #print('fecha format:',fecha_formateada)

    p_decimal= numero % 1
    #print('p_decimail:',p_decimal)
    hora= int(p_decimal*24)
    #print('hora=',hora)
    if hora <= 5 or hora >= 22:
        f=open("tabla_cut.txt", "a")
        linea=fecha_formateada+',  '+hms+',  '+ format(float(fila[3]),'.5f') + ',  '+ format(float(fila[4]),'.1f')+',  '+ format(float(fila[5]),'.1f') +',  '+format(float(fila[6]),'.1f') +',  '+ str(fila[7]) +',  '+ str(fila[8]) + ',  '+format(float(fila[9]),'.2f') +',  '+ format(float(fila[10]),'.1f') + ', '+ format(float(fila[11]),'.1f')+'\n'
        f.write(linea)
        f.close()
    else:
        #print('hora_else:', hora)
        pass
        
#usamos tabla2_fin2_copy.csv y creamos tabla_cut.txt que transformamos a tabla_cut.csv con excel. 
with open('tabla2_fin2_copy.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        #print(fila)
        if fila[1]=='date' or fila[2]=='hora' or fila[3] == 'datetime' or fila[4]=='ecs_az_pos' or fila[5]=='topshut_pos' or fila[6]=='botshut_pos' or fila[7]=='eastVent_pos' or fila[8]=='westVent_pos' or fila[9]=='pwfs2_see' or fila[10]=='windSp' or fila[11]=='windDir':
            pass
        else:
            #print(fila[0])
            numero = float(fila[3])
            fecha_legible = cutcolum(fila,numero)
            #print(fecha_legible)

