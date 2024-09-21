#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:30:58 2024
Aquí tienes un script en Python utilizando la biblioteca pandas para leer el archivo 
tabla_p2sel_fin1.csv, filtrar las filas donde los valores de la columna pwfs2_see estén 
entre 0.2 y 2, y luego guardar el resultado en un nuevo archivo CSV
output-> tabla_p2sel_fin2.csv
@author: pcandia
"""

import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('tabla_p2sel_fin1.csv')

# Filtrar las filas donde pwfs2_see tiene valores entre 0.2 y 2
filtered_df = df[(df['pwfs2_see'] >= 0.2) & (df['pwfs2_see'] <= 2)]

# Seleccionar todas las columnas
selected_columns = [
    'date', 'hour', 'datetime', 'ecs_az_pos', 'topshut_pos', 'botshut_pos',
    'eastVent_pos', 'westVent_pos', 'pwfs2_see', 'windSp', 'windDir'
]

# Crear un nuevo DataFrame con las columnas seleccionadas
result_df = filtered_df[selected_columns]

# Mostrar el DataFrame filtrado y seleccionado
#print(result_df)

# Guardar el DataFrame resultante en un nuevo archivo CSV
result_df.to_csv('tabla_p2sel_fin2.csv', index=False)
