#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:02:02 2024

@author: pcandia
"""

import pandas as pd

# Leer el archivo CSV que ya estan con las columnas completadas en ecs_az, top_shut_pos,botshut_pos
df = pd.read_csv('tabla_topsh_botsh.csv')

# Supongamos que la columna que queremos modificar se llama 'valores'
column_name = 'eastVent_pos'

# Convertir la columna a una lista para facilitar el procesamiento
values = df[column_name].tolist()

# Función para rellenar valores -0.1 con el promedio de los valores positivos y ceros contiguos
def fill_between_positives_and_zeros(values):
    n = len(values)
    i = 0
    while i < n:
        if values[i] >= 0:  # Considerar tanto positivos como cero
            start_idx = i
            start_value = values[i]
            i += 1
            # Encontrar el siguiente valor positivo o cero
            while i < n and values[i] == -0.1:
                i += 1
            if i < n and values[i] >= 0:  # Considerar tanto positivos como cero
                end_value = values[i]
                avg_value = (start_value + end_value) / 2
                # Rellenar los valores -0.1 con el promedio
                for j in range(start_idx + 1, i):
                    values[j] = avg_value
        else:
            i += 1
    return values

# Aplicar la función a los valores
df[column_name] = fill_between_positives_and_zeros(values)

# Mostrar el DataFrame modificado
#print(df[column_name])

# Guardar el DataFrame modificado en un nuevo archivo CSV si es necesario
df.to_csv('tabla_botsh_eastvent.csv', index=False)
