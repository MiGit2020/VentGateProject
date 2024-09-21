#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 12:44:44 2024

@author: pcandia
"""

import pandas as pd
df = pd.read_csv('p2mean_8ms.csv')

# Filtrar el DataFrame para cumplir con las condiciones:
# 0 < eastVent <= 10, 0 < westVent <= 10, y 90 < windDir < 270
df_filtrado = df[(df['eastVent'] > 0) & (df['eastVent'] <= 10) &
                 (df['westVent'] > 0) & (df['westVent'] <= 10) &
                 (df['windDir'] > 90) & (df['windDir'] < 270)]

# Verificar que el filtro se aplicó correctamente
print(df_filtrado[['windDir']].describe())
print(df_filtrado['windDir'])