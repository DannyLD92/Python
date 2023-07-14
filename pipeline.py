import csv
import pandas as pd
import pyodbc as oc
import os 

url= '.\\downloads\\Copia de dataPruebaDataEngineer (2) (3)\\dataPruebaDataEngineer\\' # cambiar URL de archivo

contenido = os.listdir(url) # Listar el directorio
archivo_csv = [] # vector donde se almacenaran los nombres de directorio
conn = oc.connect('Driver={SQL Server};'
                 'Server=localhost\SQLEXPRESS;'
                 'Database=Prueba;'
                 'Trusted_Connection=yes;') # conexion a BD
cursor = conn.cursor() # Constructor de cursor

#lista de variables de control 
contador = 0
sumatoria = 0
promedio = 0
maximo = 0
minimo = 9999999999
medio = 0

#Inicio de recorrido sobre los archivo
for archivo in contenido :
    if os.path.isfile(os.path.join(url, archivo)) and archivo.endswith('.csv') and archivo.startswith('2012'): #define que archivos tomar
        archivo_csv=archivo #toma el archivo
        with open(url + "" + archivo_csv, 'r') as csvfile: #apertura de archivo
            #print (url + "" + archivo_csv)
            spamreader = csv.reader(csvfile, delimiter=',') #lectura de archivo
            next(spamreader) #omitir encabezados
            fecha = ''
            id = ''
            valor = ''
            for row in  spamreader  :      #bucle para leer el archivo de inicio a fin
                #calculos de control  
                if(row[0]!='') : fecha =  row[0] 
                if(row[1]!='') : valor =  int(row[1])
                else : valor = 0 
                if(row[2]!='') : id =  row[2]
                else : id = 'null'
                sumatoria = sumatoria + valor
                contador = contador +1
                if(maximo >  0) : promedio = sumatoria / contador
                else : promedio = promedio
                if (valor > maximo) : maximo = valor
                if (valor < minimo) : minimo = valor
                if(maximo >  0) : medio =  maximo / 2  
                else: medio = medio
                #setteo de la variable que se va insertar 
                dato = ('insert into Precio values('+"cast('" +fecha+"'"+' as date),' + str(valor)  + ','+id+ ')')
                #print (dato)
                #muestreo de la validacion por ejecucion
                print ('conteo: ' + str(contador)+ ' maximo: '+ str(maximo) +" minimo: " + str(minimo) + " promedio: " + str(promedio) 
                       + " medio: "+ str(medio) )
                #Ejecucion del comando 
                cursor.execute(dato)
                #Cierre de la base de datos
                conn.commit()

