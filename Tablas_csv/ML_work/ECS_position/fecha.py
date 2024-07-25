#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
completar fecha a partir del valor decimal. Los valores que estan como -0.1 
son reemplazados por formato fecha m/d/y h:m

@author: pcandia
"""
from datetime import datetime, timedelta
import csv
#import pandas as pd
#import os,sys




def convertir_fecha_decimal(fila,numero):
    # Convertir la fecha decimal en un objeto datetime
    fecha_base = datetime(1899, 12, 30)
    delta = timedelta(days=numero)
    fecha = fecha_base + delta

    # Formatear la fecha en un formato legible
    fecha_formateada = fecha.strftime("%m/%d/%Y")
    print('numero:',numero)
    p_entera=int(numero)
    p_decimal= numero % 1
    hora= int(p_decimal*24)
    hora2 = format(hora, '02')
    min= int(((p_decimal*24) % 1)*60)
    min2 = format(min, '02')
    seg= int(((((p_decimal*24) % 1)*60) % 1)  *60)
    seg2= format(seg, '02') 
    if numero== -0.1:
        return(numero)
    
#f=open("test_p2_w.txt", "w")   
with open('f_p2_w_1_fin1.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        fila[1] == 'datetime'
        if fila[0]=='-0.1' and fila[7] == '-0.1':
            #linea=fila[0]+' '+fila[1]+' '+fila[7]+' '+fila[9]+ '\n'
            #f.write(linea)
            pass
        else:
            numero = float(fila[1])
            fecha_legible = convertir_fecha_decimal(fila,numero)
            print(fecha_legible)
            

            