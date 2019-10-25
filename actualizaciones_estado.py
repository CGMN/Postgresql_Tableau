import psycopg2

try:
    connection = psycopg2.connect(user="admin", password="admin",
                              host="localhost", port="5432", database="Gestion_RRHH")
    cursor = connection.cursor()
    print ("Se ha conectado satisfactoriamente a la base de datos","\n")

    # actualizar estado
    print ("Escriba el mes de inicio de la toma de razón, en minusculas")
    meses_anio=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']

    mes_inicio=input()

    meses_considerados=[]

    ind_inicio=meses_anio.index(mes_inicio)

    i=ind_inicio
    while i<12:
        meses_considerados.append(meses_anio[i])
        i+=1

    meses=tuple(meses_considerados)

    if mes_inicio in meses_anio:
        sql=cursor.mogrify("UPDATE presup_est SET anio = '9999' WHERE anio = '2018' AND mes IN %s;",(meses,))
        cursor.execute(sql)
        conteo=cursor.rowcount
        connection.commit()
        print ("\nSe han modificado:",conteo,"filas")
    else:
        print ("\nMes no corresponde")

except (Exception, psycopg2.Error) as error:
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("\nConexión finalizada con PostgreSQL")
