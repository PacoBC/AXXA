# -*- coding: utf-8 -*-

"""
Importacion pandas: Es utilizada para la manipulacion de los archivos .csv
Importacion numpy: Es usada para la normalización de el archivo, es usada para reemplazar el caracter \N,
                    es posible verlo en la linea: 55
Importacion os: Es utilizada para la funcionalidad dependiente del sistema operativo, manipular rutas, 
                crear archivos y directorios temporales y para el control de archivos y directorios de alto nivel.
"""
import pandas as pd
import numpy as np
import os


#Linea 17: se colocará la direccion del archivo .csv, manualmente
df = pd.read_csv('/content/incidentes_viales_2021_axa.csv', encoding='utf-8')

#Linea 21: es utilizada para eliminar todas aquillas filas que no contengan nada de información.
df = df.dropna(axis = 0, how="all")

#Linea 22: es utilizada para eliminar la columna DIA.
df = df.drop('DIA', axis = 1)

#Linea 24 -38: se hace el renombre de las columnas necesarias.
df = df.rename(columns={'CAUSA SINIESTRO': 'TIPO DE PERCANCE',
                   'PUNTO DE IMPACTO': 'PUNTO IMPACTO',
                   'AÑO': 'AÑO REPORTE',
                   'MES' : 'MES REPORTE',
                   'DÍA NUMERO' : 'DÍA REPORTE',
                   'HORA' : 'HORA REPORTE',
                   'CIUDAD' : 'CIUDAD MUNICIPIO',
                   'LESIONADOS' : 'TOTAL LESIONADOS',
                   'RELACION LESIONADOS' : 'ROL LESIONADO',
                   'NIVEL LESIONADO' : 'NIVEL LESIÓN',
                   'OBRA CIVIL' : 'DAÑO OBRA CIVIL',
                   'FUGA' : 'TERCERO FUGA',
                   'SEGURO' : 'ASEGURADORA',
                   'TAXI' : 'SERVICIO TAXI'})

#Linea 41 - 44: Creacion de columnas de tipo de variable dummie
dummies = ['AMBULANCIA', 'ARBOL', 'PIEDRA', 'DORMIDO', 'GRUA', 'DAÑO OBRA CIVIL',
       'PAVIMENTO MOJADO', 'EXPLOSION LLANTA', 'VOLCADURA', 'PERDIDA TOTAL',
       'CONDUCTOR DISTRAIDO', 'TERCERO FUGA', 'ALCOHOL', 'MOTOCICLETA',
       'BICICLETA', 'ASEGURADORA', 'SERVICIO TAXI', 'ANIMAL']

#Linea 47: Se discretiza las columnas, convirtiendolas a tipo entero
discre = ['SINIESTRO','DÍA REPORTE',	'HORA REPORTE', 'TOTAL LESIONADOS', 'EDAD LESIONADO','AÑO REPORTE']
for i in discre:
  df[i] = df[i].astype(int)

#Linea 52: Se transforman los valores NaN de las columnas dummies a 0
df[dummies] = df[dummies].fillna(0)

#Linea 55: Se transforman los caracteres \N a tipo NaN
df = df.replace(to_replace = r'\N', value =np.nan)

#Linea 57 - 60: Se discretizan las columnas especificadas en la lista discre, transformandolas a formato Camel Case
discre = ['CALLE', 'COLONIA', 'ESTADO', 'CIUDAD MUNICIPIO']
for i in discre:
  df[i]= df[i].str.upper().str.title()

#Linea 62 - 64: Se crea un directorio especifico, para guardar los reportes
anio = df['AÑO REPORTE'][0]
os.mkdir("incidentes_viales_{}_axa".format(anio))

#Linea 67 - 71: Creacion de reportes
arr = df["MES REPORTE"].unique() 
for i in arr:
  df_aux = df.loc[df['MES REPORTE'] == i]
  path = 'incidentes_viales_{}_axa/Seguridad_Vial_concatenado_{}_{}.xlsx'.format(anio, i, anio)
  df.to_excel(path, encoding='utf8')