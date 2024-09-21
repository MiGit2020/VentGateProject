#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 11:22:24 2024
Valores filtrados de P2. Selecciono solo los positivos y elimino los valores de -0.1
@author: pcandia
"""

import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('tabla_windsp.csv')

# Filtrar las filas donde pwfs2_see tiene valores positivos
filtered_df = df[df['pwfs2_see'] > 0]

# Seleccionar las columnas deseadas
selected_columns = [
    'date', 'hour', 'datetime', 'ecs_az_pos', 'topshut_pos', 'botshut_pos',
    'eastVent_pos', 'westVent_pos', 'pwfs2_see', 'windSp', 'windDir'
]

# Crear un nuevo DataFrame con las columnas seleccionadas
result_df = filtered_df[selected_columns]

# Mostrar el DataFrame filtrado y seleccionado
#print(result_df)

# Guardar el DataFrame resultante en un nuevo archivo CSV
result_df.to_csv('tabla_p2sel_fin1.csv', index=False)