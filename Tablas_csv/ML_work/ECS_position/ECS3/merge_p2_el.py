#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 10:23:53 2024

@author: pcandia
"""

import pandas as pd

# Supongamos que ya has cargado tus DataFrames

dfA = pd.read_csv('tabla_p2sel_fin2.csv')
dfB = pd.read_csv('mcs_2022_el.csv')

# Crear una lista para almacenar los resultados
resultados = []

# Iterar sobre cada fila en dfA
for i, row_A in dfA.iterrows():
    valor_A2 = row_A['datetime']
    
    # Calcular la diferencia absoluta con cada valor en colB de dfB
    diferencias = (dfB['datetime'] - valor_A2).abs()
    
    # Encontrar el índice del valor más cercano en colB
    idx_cercano = diferencias.idxmin()
    
    # Obtener el valor de colB más cercano
    valor_mas_cercano = dfB.loc[idx_cercano, 'datetime']
    valor_date= dfB.loc[idx_cercano,'date']
    valor_hour= dfB.loc[idx_cercano,'hour']
    valor_az = dfB.loc[idx_cercano,'mcs_az_pos']
    valor_el = dfB.loc[idx_cercano,'mcs_el_pos']
    
    # Combinar los datos de la fila de dfA con el valor más cercano de dfB
    resultado = {
        'date': row_A['date'],
        'hour':row_A['hour'],
        'datetime': row_A['datetime'],
        'ecs_az_pos': row_A['ecs_az_pos'],
        'topshut_pos': row_A['topshut_pos'],
        'botshut_pos': row_A['botshut_pos'],
        'eastVent_pos': row_A['eastVent_pos'],
        'westVent_pos': row_A['westVent_pos'],
        'pwfs2_see': row_A['pwfs2_see'],
        'windSp': row_A['windSp'],
        'windDir': row_A['windDir'],
        'dateB': valor_date,
        'HourB': valor_hour,
        'datetimeB': valor_mas_cercano,
        'mcs_az_pos': valor_az,
        'mcs_el_pos': valor_el,
    }
    
    # Añadir el resultado a la lista de resultados
    resultados.append(resultado)

# Convertir la lista de resultados a un DataFrame
df_resultado = pd.DataFrame(resultados)

# Mostrar el DataFrame resultado
#print(df_resultado)

df_resultado.to_csv('mcsAB_1.csv')