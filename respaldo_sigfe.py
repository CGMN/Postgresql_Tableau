import os
os.chdir('C:/Program Files/PostgreSQL/10/bin') #ojo con las / en lugar de \
os.startfile("bat_respaldo_sigfe.bat")


#se hizo un archivo .bat en la carpeta bin de PostgreSQL, el archivo contenia:
#.\pg_dump -U admin -d Gestion_RRHH -t public.sigfe_gasto_presup > 'C:\Documentos_Minsal\TABLEAU\RESPALDO BASE\respaldo_sigfe.sql'
