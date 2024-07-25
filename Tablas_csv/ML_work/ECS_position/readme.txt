gmos_pwfs2_2022.csv : contiene fecha, datetime decimal, p2 seeing

GS_ECS_20220101_0808.csv : contiene, fecha mm/dd/yy hh:mm , date time decimal, ecs_az,
                           top shutter, bottom shutter, east Vent gate and west vent gate
                           position. Posición de los Vent gates no esta redondeada.

GS-ecs_p2_merge.csv : lo mismo que GS_ECS_20220101_0808.csv salvo que aparece el p2 seeing
                      y los valores de la posición de los vengares esta redondeada.

GS_ecs_round.csv : Lo mismo que GS_ECS_20220101_0808.csv solo que la posición de los 
                   ventgates esta redondeada.


ML_ecs_1.ipynb : comandos python para ser leidos por Jupiter.

                           
GS-ecs_p2_merge.csv : lo mismo que GS-ecs_p2_merge.csv pero le agregue la columna
                      de velocidad del viento.


PC: Datos de seeing establish en utc.  Chilean-time= UTC-3 en verano y UTC-4 en invierno.


