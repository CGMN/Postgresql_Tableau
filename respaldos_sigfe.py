import psycopg2
import csv
import datetime


AUN NO FUNCIONA, TAL VEZ DONDE ES MUY GRANDE LA TABLA

try:
    connection = psycopg2.connect(user="admin", password="admin",
                              host="localhost", port="5432", database="Gestion_RRHH")
    cursor = connection.cursor()
    #Print PostgreSQL Connection properties
    #print (connection.get_dsn_parameters(),"\n")
    print ("\nSe ha conectado satisfactoriamente a la base de datos","\n")

    # respaldar bases
    print ("Grabando archivo, espere")
    postgreSQL_select_Query = "select * from sigfe_gasto_presup"
    cursor.execute(postgreSQL_select_Query)

    rows=cursor.fetchall()

    with open('respaldo_sigfe_gasto_presup_'+str(datetime.date.today())+'.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        for row in rows:
            writer.writerow(row)

    print ("La tabla 'sigfe_gasto_presup' se ha respaldado con exito",'\n')


except (Exception, psycopg2.Error) as error:
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("Conexión finalizada con PostgreSQL")
