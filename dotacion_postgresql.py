import psycopg2

try:
    connection = psycopg2.connect(user="admin", password="admin",
                              host="localhost", port="5432", database="Gestion_RRHH")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print (connection.get_dsn_parameters(),"\n")
    print ("Se ha conectado satisfactoriamente a la base de datos","\n")
    # subir csv
    print ("¿Está seguro que desea subir el archivo dotacion_para_subir.csv a la tabla new_cupos_est?")
    print ("Responda: SI o NO","\n")
    respuesta=input()
    if respuesta=='SI':
        with open('dotacion_para_subir.csv', 'r') as f:
            cursor.copy_from(f, 'new_cupos_est', sep=',')
            connection.commit()
            print ("Se ha agregado la información a la tabla","\n")
    else:
        print ("No se ha realizado la acción")

except (Exception, psycopg2.Error) as error:
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("Conexión finalizada con PostgreSQL")
