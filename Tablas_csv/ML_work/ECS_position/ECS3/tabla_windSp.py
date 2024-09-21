#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 21:10:29 2024

@author: pcandia
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 21:10:29 2024

@author: pcandia
"""

import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('tabla_westvent_windDir.csv')

# Supongamos que la columna que queremos modificar se llama 'windSp'
column_name = 'windSp'

# Convertir la columna a una lista para facilitar el procesamiento
values = df[column_name].tolist()

# Función para rellenar valores -0.1 con el valor cero o positivo adyacente siguiente
def fill_with_next_positive_or_zero(values):
    n = len(values)
    i = 0
    while i < n:
        if values[i] >= 0:
            next_non_negative = values[i]
            i += 1
            # Encontrar el siguiente valor cero o positivo
            while i < n and (values[i] == -0.1):
                values[i] = next_non_negative
                i += 1
            if i < n and values[i] >= 0:
                next_non_negative = values[i]
        else:
            i += 1
    return values

# Aplicar la función a los valores
df[column_name] = fill_with_next_positive_or_zero(values)

# Mostrar el DataFrame modificado
print(df)

# Guardar el DataFrame modificado en un nuevo archivo CSV si es necesario
df.to_csv('tabla_windsp.csv', index=False)
