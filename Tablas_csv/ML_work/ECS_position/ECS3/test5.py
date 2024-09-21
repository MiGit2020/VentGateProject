#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:11:35 2024

@author: pcandia
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('test5.csv')

def categorizar_east(K):
    if 3 < K <= 6:
        return '50-60'

df['East_Range'] = df['K'].apply(categorizar_east)
print(df)

# Graficar windSpeed versus p2mean, coloreando según los rangos de eastVent
sns.lmplot(x='K', y='J', data=df, hue='East_Range', fit_reg=False, height=4, aspect=1.0)

# Añadir título y etiquetas
plt.title('Gráfico de windSpeed vs p2mean con Rangos de eastVent')
plt.xlabel('windSpeed (m/s)')
plt.ylabel('p2mean')

# Mostrar el gráfico
plt.show()