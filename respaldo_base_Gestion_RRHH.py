import os
os.chdir('C:/Program Files/PostgreSQL/10/bin') #ojo con las / en lugar de \
os.startfile("bat_respaldo_base.bat")


#se hizo un archivo .bat en la carpeta bin de PostgreSQL, el archivo contenia:
# .\pg_dump -U admin -W -F p Gestion_RRHH > "C:\Documentos_Minsal\TABLEAU\RESPALDO BASE\respaldo_base_Gestion_RRHH.sql"
# PAUSE
