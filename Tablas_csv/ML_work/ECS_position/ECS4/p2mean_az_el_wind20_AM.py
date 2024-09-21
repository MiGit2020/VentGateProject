#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:23:09 2024
Script para calcular la masa de aire AM usando el angulo de elevacion del telescopio.
@author: pcandia
"""

import pandas as pd
import numpy as np

# Leer el archivo CSV
file_path = 'p2mean_az_el_wind20.csv'  # Reemplaza con la ruta correcta de tu archivo
df = pd.read_csv(file_path)

# Calcular el ángulo cenital z = 90 - mcs_el_pos
df['zenith_angle'] = 90 - df['mcs_el_pos']

# Calcular la masa de aire AM = 1 / cos(z)
df['AM'] = 1 / np.cos(np.radians(df['zenith_angle']))

# Guardar el resultado en un nuevo archivo CSV (opcional)
output_file = 'p2mean_az_el_wind20_AM.csv'
df.to_csv(output_file, index=False)

# Mostrar las primeras filas del DataFrame para verificar
#print(df[['mcs_el_pos', 'zenith_angle', 'AM']].head())