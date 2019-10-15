import csv
import pandas as pd
import numpy as np
import tkinter.filedialog
import re

#la entrada es archivo con cod ss, cod establ, glosa y valor
#convertirlo a formato de subida

# para agrupar, se debe escribir agrupor y luego tab

print("Ingrese el año en números")
anio = input()
print("Ingrese el mes (use minúsculas)")
mes = input()

#lectura y preparación (OK)
#<inicio #
root = tkinter.Tk()
root.withdraw()
file_path = tkinter.filedialog.askopenfilename()

print("")
print("leyendo base\n")

# el archivo debería tener este formato: Cod SS, Cod Estab, Glosa,Valor,
#importa el orden, no el nombre
dfdot = pd.read_excel(str(file_path))

dfdot.loc[0, "SS"] = ""
dfdot.loc[0, "Establ"] = ""
dfdot.loc[0, "Cod Dipres"] = ""

#</fin #


#uso de diccionarios (OK)
#<inicio #

# diccionarios
df1 = pd.read_excel("Estandarización.xlsx",
                    sheet_name="SS y Establ QV a Tableau")
df2 = pd.read_excel("Estandarización.xlsx", sheet_name="Glosas QV a Tableau")
cabeceras1 = (list(df1))  # lista con las cabeceras
cabeceras2 = (list(df2))  # lista con las cabeceras

diccio_SS = {}  # crea el diccionario de cod servicio:servicio de salud
for i in range(0, len(df1)):
    diccio_SS[df1.loc[i, str(cabeceras1[0])]
                 ] = df1.loc[i, str(cabeceras1[2])]

diccio_codDipres = {} #diccionario cod ss: cod dipres
for i in range(0, len(df1)):
    diccio_codDipres[df1.loc[i, str(cabeceras1[0])]
                     ] = df1.loc[i, str(cabeceras1[1])]

diccio_establ = {}  # diccionario cod establ:nombre establ logra
for i in range(0, len(df1)):
    diccio_establ[df1.loc[i, str(cabeceras1[8])]
                  ] = df1.loc[i, str(cabeceras1[9])]

#uso de los diccionarios
dfdot[dfdot.columns[4]].update(dfdot[dfdot.columns[0]].map(
    diccio_SS))  # cod ss - servicio de salud

dfdot[dfdot.columns[5]].update(dfdot[dfdot.columns[1]].map(
    diccio_establ))  # cod establ - establ

dfdot[dfdot.columns[6]].update(dfdot[dfdot.columns[0]].map(
    diccio_codDipres))  # cod ss - cod dipres

#</fin #


#llevar los datos de dotacion al formato (OK)
#<inicio #

df_formato = pd.read_excel("FORMATO DOTACION.xlsx")

df_formato[['CÓDIGO SIRH DEL SERVICIO DE SALUD', 'CÓDIGO SIRH DEL ESTABLECIMIENTO',
            'Glosa', 'Devengado Moneda Año Estudio (2019)', ' Institucion Logra', 'Establecimiento Logra',
            'CÓDIGO DIPRES DEL SERVICIO DE SALUD']] = dfdot[['Cod SS', 'Cod Establ', 'Glosa', 'Valor',
                                                            'SS', 'Establ', 'Cod Dipres']]

df_formato['año '] = anio
df_formato['mes'] = mes
df_formato.fillna(0, inplace=True)

#</fin #


#grabar archivo (OK)
#<inicio #

dfdot.to_csv('dotacion.csv', encoding='latin1', index=False)
print ('Archivo grabado')

df_formato.to_csv('dotacion_para_subir.csv', encoding='latin1',
                  index=False, header=False)


#</fin #
