#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:47:22 2024

@author: pcandia
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:01:23 2024
Este script calcula el la media de P2 para un tiempo especifico que se tiene que
elejir, el cual se coloca en Timedelta(seconds= ??). El script ademas de calcular
la media en el datetime selecciona el datetime mas cercano al valor. De esta forma 
el datetime tiene la fila completa para realizar los plots necesarios. El valor 
del datetime mas cercano a la media esta en la columna Adjusted Timestamp.
@author: pcandia

input--> mcs_az_el_wind20.csv
output --> p2mean_az_el.csv
"""

import pandas as pd

# Leer el archivo CSV
file_path = 'mcs_az_el_wind20.csv'  # Reemplaza con la ruta correcta de tu archivo
df = pd.read_csv(file_path)

# Eliminar espacios en blanco al principio de la columna C (hora)
df['hour'] = df['hour'].str.strip()

# Convertir la columna B (fecha) y la columna C (hora) a formato de tiempo
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%y')
df['hour'] = pd.to_datetime(df['hour'], format='%H:%M:%S').dt.time

# Combinar la fecha de la columna B y la hora de la columna C en un solo timestamp
df['timestamp'] = df.apply(lambda row: pd.Timestamp.combine(row['date'], row['hour']), axis=1)

# Calcular el tiempo inicial
start_time = df['timestamp'].min()

# Crear una lista para almacenar los resultados
resultados = []

# Calcular la media en intervalos de 80 segundos
while start_time < df['timestamp'].max():
    # Definir el intervalo
    end_time = start_time + pd.Timedelta(seconds=120)
    
    # Filtrar las filas que caen dentro del intervalo
    df_interval = df[(df['timestamp'] >= start_time) & (df['timestamp'] < end_time)]
    
    if not df_interval.empty:
        # Calcular la media de la columna J en el intervalo
        mean_value = df_interval['pwfs2_see'].mean()
        
        # Calcular el timestamp promedio entre start_time y end_time
        mean_timestamp = start_time + (end_time - start_time) / 2
        
        # Determinar el timestamp ajustado según las reglas proporcionadas
        if len(df_interval) == 1:
            adjusted_timestamp = df_interval['timestamp'].iloc[0]
        elif len(df_interval) == 2:
            adjusted_timestamp = df_interval['timestamp'].iloc[0]
        else:
            # Encontrar el timestamp más cercano al mean_timestamp
            adjusted_timestamp = df_interval.iloc[(df_interval['timestamp'] - mean_timestamp).abs().argsort()[:1]]['timestamp'].values[0]
        
        # Calcular el error como la diferencia entre mean_timestamp y start_time
        error = mean_timestamp - start_time
        
        # Crear un diccionario para la nueva fila con la estructura adecuada
        new_row = {
            'id': df_interval.iloc[0]['id'],
            'date': df_interval.iloc[0]['date'],
            'hour': df_interval.iloc[0]['hour'],  # Convertir fecha a formato mm/dd/yy
            'datetime': df_interval.iloc[0]['datetime'],
            'ecs_az': df_interval.iloc[0]['ecs_az_pos'],
            'topshut': df_interval.iloc[0]['topshut_pos'],
            'botshut': df_interval.iloc[0]['botshut_pos'],
            'eastVent': df_interval.iloc[0]['eastVent_pos'],
            'westVent': df_interval.iloc[0]['westVent_pos'],
            'pwfs2_see': df_interval.iloc[0]['pwfs2_see'],
            'windSpeed': df_interval.iloc[0]['windSp'],
            'windDir': df_interval.iloc[0]['windDir'],
            'p2_mean': mean_value,  # La media en la columna J
            'Error': error.total_seconds(),  # El error en segundos
            'Adjusted Timestamp': adjusted_timestamp,  # El timestamp ajustado
            'dateB': df_interval.iloc[0]['dateB'],
            'hourB': df_interval.iloc[0]['HourB'],
            'datetimeB': df_interval.iloc[0]['datetimeB'],
            'mcs_el_pos': df_interval.iloc[0]['mcs_el_pos']
        }
        
        # Añadir la nueva fila resultante a la lista de resultados
        resultados.append(new_row)
    
    # Avanzar al siguiente intervalo
    start_time = end_time

# Crear un DataFrame con las filas resultantes
result_df = pd.DataFrame(resultados)

# Guardar el resultado en un archivo CSV con el formato solicitado
output_file = 'p2mean_az_el_wind20.csv'  # Reemplaza con la ruta deseada para guardar el archivo
result_df.to_csv(output_file, index=False)

# Mostrar el resultado para verificar
print(result_df)