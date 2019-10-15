import csv
import pandas as pd
import numpy as np
import tkinter.filedialog
import re

# para agrupar, se debe escribir agrupar y luego tab

print("Ingrese el año en números")
anio = input()
print("Ingrese el mes (use minúsculas)")
mes = input()

# Leer archivo de Qv, usar diccionarios OK
#<inicio #
root = tkinter.Tk()
root.withdraw()
file_path = tkinter.filedialog.askopenfilename()

print("")
print("leyendo base\n")

# el archivo debería tener este formato: Servicio de Salud, Establecimiento, Haber, Valor,
#importa el orden, no el nombre
dfqv = pd.read_excel(str(file_path))

# print(dfqv.columns.tolist())

dfqv.loc[0, "Cod SS"] = ""
dfqv.loc[0, "Cod Establ"] = ""
dfqv.loc[0, "Glosa"] = ""
dfqv.loc[0, 'Cod Dipres'] = ""
dfqv.loc[0, 'Establ'] = ""
#
# diccionarios
df1 = pd.read_excel("Estandarización.xlsx",
                    sheet_name="SS y Establ QV a Tableau")
df2 = pd.read_excel("Estandarización.xlsx", sheet_name="Glosas QV a Tableau")
cabeceras1 = (list(df1))  # lista con las cabeceras
cabeceras2 = (list(df2))  # lista con las cabeceras

diccio_codSS = {}  # crea el diccionario de nombre servicio de salud:cod servicio
for i in range(0, len(df1)):
    diccio_codSS[df1.loc[i, str(cabeceras1[2])]
                 ] = df1.loc[i, str(cabeceras1[0])]

diccio_codest = {}  # diccionario nombre establ:cod establ
for i in range(0, len(df1)):
    diccio_codest[df1.loc[i, str(cabeceras1[6])]
                  ] = df1.loc[i, str(cabeceras1[8])]

diccio_establ = {}  # diccionario cod establ:nombre establ logra
for i in range(0, len(df1)):
    diccio_establ[df1.loc[i, str(cabeceras1[8])]
                  ] = df1.loc[i, str(cabeceras1[9])]

diccio_codDipres = {}
for i in range(0, len(df1)):
    diccio_codDipres[df1.loc[i, str(cabeceras1[0])]
                     ] = df1.loc[i, str(cabeceras1[1])]

diccio_glosa = {}  # diccionario haber:glosa
for i in range(0, len(df2)):
    diccio_glosa[df2.loc[i, str(cabeceras2[0])]
                 ] = df2.loc[i, str(cabeceras2[1])]

# uso de los diccionarios
dfqv[dfqv.columns[4]].update(dfqv[dfqv.columns[0]].map(
    diccio_codSS))  # cod ss - servicio de salud
dfqv[dfqv.columns[5]].update(dfqv[dfqv.columns[1]].map(
    diccio_codest))  # cod establ - establecimiento
dfqv[dfqv.columns[6]].update(dfqv[dfqv.columns[2]].map(
    diccio_glosa))  # glosa - Haber
dfqv[dfqv.columns[8]].update(dfqv[dfqv.columns[5]].map(
    diccio_establ))  # Establ - Cod Establecimiento
dfqv[dfqv.columns[7]].update(dfqv[dfqv.columns[4]].map(
    diccio_codDipres))  # cod dipres -  cod SS

#</fin #


# Leer formato cupos OK
#<inicio #

df_formato = pd.read_excel("FORMATO CUPOS.xlsx")

# print(df_formato.columns.tolist())

#</fin #


# llevar los valores del archivo de cupos a formato cupos OK
#<inicio #

df_formato[['CÓDIGO SIRH DEL SERVICIO DE SALUD', 'CÓDIGO SIRH DEL ESTABLECIMIENTO',
            'Glosa', 'Devengado Moneda Año Estudio (2019)', ' Institucion Logra', 'Establecimiento Logra',
            'CÓDIGO DIPRES DEL SERVICIO DE SALUD']] = dfqv[['Cod SS', 'Cod Establ', 'Glosa', 'Valor',
                                                            'Servicio de Salud ', 'Establ', 'Cod Dipres']]

df_formato['año '] = anio
df_formato['mes'] = mes
df_formato.fillna(0, inplace=True)

#</fin #


# grabar archivos OK
#<inicio #

dfqv.to_csv('cupos.csv', encoding='latin1', index=False)

df_formato.to_csv('cupos_para_subir.csv', encoding='latin1',
                  index=False, header=False)

print("")
print("Archivo grabado con el nombre 'cupos_para_subir.csv'")

#</fin #
