#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:10:20 2024
código en Python que realiza el cálculo del seeing corregido al cenit (IQ_zenith) utilizando la fórmula:

IQ(zenith)=IQ(X)/AM^0.6
@author: pcandia
"""

import pandas as pd
import numpy as np

# Ruta al archivo CSV
file_path = 'p2mean_az_el_wind20_AM.csv'  # Asegúrate de que la ruta sea correcta

# Leer el archivo CSV
df = pd.read_csv(file_path)

# Verificar que las columnas necesarias existen
if 'AM' not in df.columns or 'p2_mean' not in df.columns:
    raise ValueError("El archivo CSV debe contener las columnas 'AM' y 'p2_mean'.")

# Calcular el seeing corregido al cenit IQ(zenith) = IQ(X) / X^0.6
df['IQ_zenith'] = df['p2_mean'] / (df['AM'] ** 0.6)

# Opcional: Guardar el DataFrame actualizado en un nuevo archivo CSV
output_file = 'p2mean_az_el_wind20_AM_IQ_zenith.csv'
df.to_csv(output_file, index=False)
print(f"El archivo con la columna 'IQ_zenith' ha sido guardado como '{output_file}'.")

# Mostrar las primeras filas del DataFrame para verificar
print(df[['AM', 'p2_mean', 'IQ_zenith']].head())