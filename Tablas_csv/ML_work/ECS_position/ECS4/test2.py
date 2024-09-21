#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:41:32 2024

@author: pcandia
"""

#%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

# Crear una figura y un eje
fig, ax = plt.subplots(figsize=(6, 6))

# Dibujar el círculo principal
circle = plt.Circle((0, 0), 1, color='lightgray', fill=True)
ax.add_artist(circle)

# Crear las franjas oscuras y con líneas más gruesas
# En las coordenadas que mencionas:
# 0 grados en +Y (parte superior), 90 grados en +X (derecha),
# 180 grados en -Y (abajo), 270 grados en -X (izquierda)
angles = [(160, 260), (320, 80)]

for start_angle, end_angle in angles:
    if start_angle > end_angle:
        # Dividir la franja en dos para manejar el cruce por 0 grados
        theta1, theta2 = start_angle, 360
        ax.add_patch(Wedge((0, 0), 1, theta1=theta1, theta2=theta2, color='black', width=0.3))
        theta1, theta2 = 0, end_angle
        ax.add_patch(Wedge((0, 0), 1, theta1=theta1, theta2=theta2, color='black', width=0.3))
    else:
        ax.add_patch(Wedge((0, 0), 1, theta1=start_angle, theta2=end_angle, color='black', width=0.3))

# Configurar el eje con coordenadas claras
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal', 'box')
ax.axis('off')

# Agregar etiquetas para mayor claridad en las coordenadas
ax.text(0, 1.1, '0° (+Y)', ha='center', va='center')
ax.text(1.1, 0, '90° (+X)', ha='center', va='center')
ax.text(0, -1.1, '180° (-Y)', ha='center', va='center')
ax.text(-1.1, 0, '270° (-X)', ha='center', va='center')

# Mostrar el gráfico
plt.show()