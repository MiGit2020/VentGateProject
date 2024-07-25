from datetime import datetime, timedelta

import csv
import pandas as pd
import os,sys

#Script para cortar una tabla en rangos de horas. En este caso las filas entre las 6am-20pm 
#seran descartadas

def convertir_fecha_decimal(fila,numero):
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
    if hora >= 6 and hora <= 20:
        return(fecha_formateada,hora2,min2,seg2,numero)
    else:
        #print("--> ",fila)
        #f=open("f_p2_w_1_fin3.txt", "a")
        f=open("proc2_f_p2_w_2_fin1.txt", "a")
        linea=fecha_formateada+',  '+hora2+':'+min2+':'+seg2+',  '+ format(float(fila[1]),'.5f') + ',  '+ format(float(fila[2]),'.1f')+',  '+ format(float(fila[3]),'.1f') +',  '+format(float(fila[4]),'.1f') +',  '+ str(fila[5]) +',  '+ str(fila[6]) + ',  '+format(float(fila[7]),'.2f') +',  '+ format(float(fila[8]),'.1f') + '\n'
        #linea=fecha_formateada+' '+hora2+':'+min2 +' '+ format(float(fila[1]),'.5f')+' '+ format(float(fila[2]),'.1f') +' '+ format(float(fila[3]),'.1f') +' '+format(float(fila[4]),'.1f') +' '+format(float(fila[5]),'.1f') +' ' +format(float(fila[6]),'.1f') +' '+fila[8]+ ' ' +fila[10] + '\n'
        f.write(linea)
        f.close()
            
            
#os.remove('/Users/pcandia/PythonScripts/test_out3.csv') 
#os.remove('/Users/pcandia/Documents/GEMINI/Proyecto/Ventgates/tablas/VentGateProject/Tablas_csv/ML_work/ECS_position/f_p2_w_1_fin2.txt')         


with open('proc2_f_p2_w_2.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)
        #if fila[0]=='fecha' or fila[1] == 'hour' or fila[2] == 'datetime' or fila[3]=='ecs_az_pos' or fila[4]=='topshut_pos' or fila[5]=='botshut_pos' or fila[6]=='eastVent_pos' or fila[7]=='westVent_pos' or fila[8]=='pwfs2_see' or fila[9]=='windAve':
        if fila[0]=='fecha' or fila[1] == 'datetime' or fila[2]=='ecs_az_pos' or fila[3]=='topshut_pos' or fila[4]=='botshut_pos' or fila[5]=='eastVent_pos' or fila[6]=='westVent_pos' or fila[7]=='pwfs2_see' or fila[8]=='windAve':
            pass
        else:
            #print(fila[0])
            numero = float(fila[1])
            fecha_legible = convertir_fecha_decimal(fila,numero)
            print(fecha_legible)

