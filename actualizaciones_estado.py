import psycopg2

try:
    connection = psycopg2.connect(user="admin", password="admin",
                              host="localhost", port="5432", database="Gestion_RRHH")
    cursor = connection.cursor()
    print ("Se ha conectado satisfactoriamente a la base de datos","\n")

    # actualizar estado
    print ("\nEscriba el mes de inicio de la toma de razón, en minusculas")
    meses_anio=['enero','febrero','marzo','abril','mayo','junio','julio','agosto',
    'septiembre','octubre','noviembre','diciembre']

    mes_inicio=input()

    if mes_inicio in meses_anio:
        print ("\nEscriba el documento que cambiará a toma de razon, en números")
        documento=int(input())

        if isinstance(documento, int):
            meses_considerados=[]

            ind_inicio=meses_anio.index(mes_inicio) #para obtener la posición del mes en la lista de meses

            #agrega los meses desde el inicio hasta diciembre
            i=ind_inicio
            while i<12:
                meses_considerados.append(meses_anio[i])
                i+=1

            meses=tuple(meses_considerados) #transforma el listado en una tupla

            sql=cursor.mogrify("""UPDATE presup_est_ultimo SET estado_documento = 'Tomado de Razón' WHERE
            estado_documento = 'Trámite' AND mes IN %s AND doc_subse=%s;""",(meses,documento))
            cursor.execute(sql)
            conteo=cursor.rowcount
            connection.commit()
            if conteo==0:
                print ("\nNo se han realizado modificaciones, asegurese de haber ingresado los datos correctamente")
            else:
                print ("\nSe han modificado:",conteo,"filas")
        else:
            print ("Debe escribir un número entero")
    else:
        print ("\nMes no corresponde")

except (Exception, psycopg2.Error) as error:
    print ("\nError while connecting to PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("\nConexión finalizada con PostgreSQL")
