#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 22:23:08 2024

@author: pcandia
"""

import pandas as pd

# Supongamos que ya has cargado tus DataFrames dfA y dfB
dfA = pd.DataFrame({
    'colA1': ['a', 'b'],
    'colA2': [2, 4]
})

dfB = pd.DataFrame({
    'colB1': [1, 2.1, 2.7, 3.9, 4.5],
    'colB2': ['b1', 'b21', 'b27', 'b39', 'b45']
})

# Crear una lista para almacenar los resultados
resultados = []

# Iterar sobre cada fila en dfA
for i, row_A in dfA.iterrows():
    valor_A2 = row_A['colA2']
    
    # Calcular la diferencia absoluta con cada valor en colB1 de dfB
    diferencias = (dfB['colB1'] - valor_A2).abs()
    
    # Encontrar el índice del valor más cercano en colB1
    idx_cercano = diferencias.idxmin()
    
    # Obtener los valores de colB1 y colB2 más cercanos
    valor_mas_cercano_colB1 = dfB.loc[idx_cercano, 'colB1']
    valor_mas_cercano_colB2 = dfB.loc[idx_cercano, 'colB2']
    
    # Combinar los datos de la fila de dfA con los valores más cercanos de dfB
    resultado = {
        'colA1': row_A['colA1'],
        'colA2': row_A['colA2'],
        'colB1_mas_cercano': valor_mas_cercano_colB1,
        'colB2_asociado': valor_mas_cercano_colB2
    }
    
    # Añadir el resultado a la lista de resultados
    resultados.append(resultado)

# Convertir la lista de resultados a un DataFrame
df_resultado = pd.DataFrame(resultados)

# Mostrar el DataFrame resultado
print(df_resultado)