import csv
import pandas as pd
import numpy as np
import tkinter.filedialog, re

root = tkinter.Tk()
root.withdraw()
file_path = tkinter.filedialog.askopenfilename()

print("")
print ("leyendo base\n")


#crear tantas copias como meses queden para llegar a diciembre (OK)
#<inicio #

meses=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']

dfmodpresup = pd.read_excel(str(file_path))

mes_in=list(set(dfmodpresup['mes'].tolist()))
print (mes_in)

ind_inicio=meses.index(mes_in[0])
print(ind_inicio)

dfmeses=[]
for i in range(ind_inicio,len(meses)):
    dfmeses.append(dfmodpresup.copy())
print ("cantidad de df por meses",len(dfmeses))

#</fin #


#cambiar en las copias de acuerdo a los meses que faltan (OK)
#<inicio #

for i in range (1, len(dfmeses)):
    dfmeses[i].replace(mes_in,meses[ind_inicio+i], inplace=True)

#</fin #


#concatenar (OK)
#<inicio #

df_consolidado=pd.concat(dfmeses)

#</fin #


#grabar (OK)
#<inicio #

df_consolidado.to_csv('modif_presup_para_subir_consolidada.csv', encoding='latin1',
                  index=False, header=False)

print ("Archivo grabado con el nombre: modif_presup_para_subir.csv")

#</fin #
