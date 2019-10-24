import psycopg2

try:
    connection = psycopg2.connect(user="admin", password="admin",
                              host="localhost", port="5432", database="Gestion_RRHH")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    #print (connection.get_dsn_parameters(),"\n")
    print ("Se ha conectado satisfactoriamente a la base de datos","\n")
    # actualizar estado

    #entrada de mes desde el que se toma razon

    print ("Escriba el mes de inicio de la toma de razón, en minusculas")
    mes_inicio=input()

    cursor.execute("UPDATE presup_est SET anio = '9999' WHERE anio = '2018' AND mes IN('octubre','noviembre','diciembre')")
    connection.commit()
    print ("Se han realizado los cambios")


except (Exception, psycopg2.Error) as error:
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("Conexión finalizada con PostgreSQL")
