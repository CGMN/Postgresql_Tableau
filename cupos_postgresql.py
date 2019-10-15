import psycopg2

try:
    connection = psycopg2.connect(user="admin", password="admin",
                              host="localhost", port="5432", database="Gestion_RRHH")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print (connection.get_dsn_parameters(),"\n")

    # subir csv

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
