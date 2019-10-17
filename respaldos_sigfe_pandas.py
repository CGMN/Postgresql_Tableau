import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd
import csv
import datetime

aun no
try:
    connection = pg.connect(user="admin", password="admin",
                              host="localhost", port="5432", database="Gestion_RRHH")
    cursor = connection.cursor()
    print ("\nSe ha conectado satisfactoriamente a la base de datos","\n")

    # respaldar bases
    print ("Grabando archivo, espere")

    #dataframe = psql.DataFrame("SELECT * FROM new_cupos_est", connection)
    # Create empty list

    query="SELECT * FROM new_cupos_est"
    dfl = []

    # Create empty dataframe
    dfs = pd.DataFrame()

    # Start Chunking
    for chunk in pd.read_sql(query, con=cursor, chunksize=100000):
        # Start Appending Data Chunks from SQL Result set into List
        dfl.append(chunk)

    # Start appending data from list to dataframe
    dfs = pd.concat(dfl, ignore_index=True)

    print (len(dfs))
    #postgreSQL_select_Query = "select * from new_cupos_est"
    #cursor.execute(postgreSQL_select_Query)

    #df.to_csv('respaldo_sigfe_gasto_presup_pandas.csv', encoding='latin1', index=False)


    print ("La tabla 'sigfe_gasto_presup' se ha respaldado con exito",'\n')


except (Exception, pg.Error) as error:
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            #cursor.close()
            connection.close()
            print("Conexión finalizada con PostgreSQL")
