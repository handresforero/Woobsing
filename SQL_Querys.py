#cd D:\Woobsing\LongTail
#conda activate LongTail

# import pymysql
# import pymysql.cursors
# import csv 
# from collections import Counter
# import collections
# from collections import defaultdict

# databaseServerIP = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'  # IP address of the MySQL database server
# databaseUserName = 'aforero'      # User name of the database server
# databaseUserPassword = 'wz5LeyV4TkDGq7<r'          # Password for the database user
# newDatabaseName = 'LongTail' # Name of the database that is to be created
# charSet = 'utf8mb4'     # Character set
# cusrorType = pymysql.cursors.DictCursor


# db = pymysql.connect(host=databaseServerIP,
#                              user=databaseUserName,
#                              password=databaseUserPassword,
#                              database=newDatabaseName,
#                              charset=charSet,
#                              cursorclass=cusrorType)

# cursor = db.cursor()
# cursor.execute("SELECT urls FROM LongTail.LongTailTable4 LIMIT 0, 100")
# myresult = cursor.fetchall()
# print(myresult)

# # res = defaultdict(int)
# # for key, val in myresult.items():
# #     res[val] += 1
# # print("The frequency dictionary : " + str(dict(res)))

# # counter= collections.Counter(myresult)
# # print(counter)
# db.close()

####################################################################################################################
####################################################################################################################
####################################################################################################################
#CONSULTAR Y TRAER DATA  #######################################################################################

# import pymysql
# from collections import Counter
# from urllib.parse import urlparse


# endpoint = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'
# username = 'aforero'
# password = 'wz5LeyV4TkDGq7<r'
# database_name = 'elnotilong'

# connection = pymysql.connect(host=endpoint, user=username, passwd=password, db=database_name)
# cursor = connection.cursor()
                 
      
# cursor.execute("SELECT IdBusqueda, contenido FROM elnotilong.paginaPulzo WHERE IdBusqueda = 29")
        
# myresult = cursor.fetchall()
# print(myresult)

####################################################################################################################
####################################################################################################################
####################################################################################################################
#AGREGAR NUEVA COLUMNA #######################################################################################

# import pymysql
# import re
# from timeit import default_timer

# databaseServerIP = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'  
# databaseUserName = 'aforero'      
# databaseUserPassword = 'wz5LeyV4TkDGq7<r'          
# newDatabaseName = 'LongTail' 
# charSet = 'utf8mb4'     
# cusrorType = pymysql.cursors.DictCursor

# db = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword, database=newDatabaseName, charset=charSet, cursorclass=cusrorType)
# cursor = db.cursor()        

# #### ADD NEW COLUMN    #######################################################################################  
# # cursor.execute("ALTER TABLE LongTail.LongTailTable4 ADD url_codf longtext")
# # #cursor.execute("ALTER TABLE LongTail.LongTailTable4 ADD id_Key INT PRIMARY KEY AUTO_INCREMENT") #add primary key and consecutive values
# # db.commit()    
# # myresult = cursor.fetchall()
# # db.close()
# # print("NEW COLUMN ADDED..")

# # ##### ADD DATA IN NEW COLUM #######################################################################################
# # sql = 'INSERT INTO LongTailTable4 (url_codf) VALUES (%s)'
# # cursor.execute(sql)
# # db.commit()
# # db.close()

# # #OBTENER EL ULTIMO REGISTRO #######################################################################################
# # cursor.execute("SELECT * FROM LongTail.LongTailTable4 ORDER BY id DESC LIMIT 1")
# # myresult = cursor.fetchone()
# # db.close()
# # print(myresult)


# #CAMBIAR DATA DE UN REGISTRO EXISTENTE#############################################################################
# # cursor.execute("UPDATE LongTail.LongTailTable4 SET url_codf = 'ZORRA' WHERE id_Key=1")
# # cursor.execute("SELECT * FROM LongTail.LongTailTable4 WHERE id_Key=1")
# # myresult = cursor.fetchone()
# # db.commit()
# # db.close()
# # print(myresult)
# i = 1
# inicio = default_timer()
# while i <= 80000:
#     print(i)
#     cursor.execute("SELECT urls FROM LongTail.LongTailTable4 WHERE id_Key= %s",(i))
#     myresult = cursor.fetchone()
#     listOfValues = myresult.values() #convertir valores de diccionario a lista
#     listOfValues = list(listOfValues)
#     listOfValues = str(listOfValues[0])
#     #print(listOfValues)
    
#     substring1 = "&amp"
#     substring2 = "\\x26amp"
#     substring3 = ".</div"
#     substring4 = "\xa0...<"
    
#     if substring1 in listOfValues:
#         result = re.split(r"&amp", listOfValues, maxsplit=1)
#     else:
#         if substring2 in listOfValues:
#             result = re.split(r"\\x26amp", listOfValues, maxsplit=1)
#         else:
#             if substring3 in listOfValues:
#                 result = re.split(r".</div", listOfValues, maxsplit=1)
#             else:
#                 if substring4 in listOfValues:
#                     result = re.split(r"\xa0...<", listOfValues, maxsplit=1)     

#     #result = re.split(r"&amp", listOfValues, maxsplit=1)
#     #result = re.split(r"\\x26amp", listOfValues, maxsplit=1)
#     #result = re.split(r".</div", listOfValues, maxsplit=1)
#     #result = re.split(r"\xa0...<", listOfValues, maxsplit=1)
#     result = result[0]

#     cursor.execute("UPDATE LongTail.LongTailTable4 SET url_codf = %s WHERE id_Key= %s",(result,i))
#     cursor.execute("SELECT * FROM LongTail.LongTailTable4 WHERE id_Key=1")
#     myresult = cursor.fetchone()
#     db.commit()
#     i += 1
# db.close()
# fin = default_timer()
# print("Programa terminado", fin-inicio)



# # cursor.execute("SELECT id, urls FROM LongTail.LongTailTable4 WHERE id = 1")
# # myresult = cursor.fetchall()

# # # for result in myresult:
# # #     urls = result[1]
# # #     print(urls)

# # db.close()
# # print(myresult)

####################################################################################################################
####################################################################################################################
####################################################################################################################
#CREATE NEW TABLE WITH VARIABLES ################################################################################

# import pymysql
# import re
# from timeit import default_timer

# databaseServerIP = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'  
# databaseUserName = 'aforero'      
# databaseUserPassword = 'wz5LeyV4TkDGq7<r'          
# newDatabaseName = 'LongTail' 
# charSet = 'utf8mb4'     
# cusrorType = pymysql.cursors.DictCursor

# db = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword, database=newDatabaseName, charset=charSet, cursorclass=cusrorType)
    
# try:
#     cursorObject = db.cursor()
#     sqlQuery = "CREATE TABLE ParseContent(id_Key INT PRIMARY KEY AUTO_INCREMENT, idbefore int, domain longtext, urls longtext, title longtext, h1 longtext, meta longtext, parrafos longtext, url_imagenes longtext)"
#     cursorObject.execute(sqlQuery)
#     sqlQuery = "show tables"
#     cursorObject.execute(sqlQuery)
#     rows = cursorObject.fetchall()

#     for row in rows:
#         print(row)

# except Exception as e:
#     print("Exeception occured:{}".format(e))

# finally:
#     db.close()

####################################################################################################################
####################################################################################################################
####################################################################################################################
#INSERT VSALUES BETWEEN TABLES ################################################################################

# import pymysql
# import re
# from timeit import default_timer
# import pandas as pd
# from csv import reader

# databaseServerIP = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'  
# databaseUserName = 'aforero'      
# databaseUserPassword = 'wz5LeyV4TkDGq7<r'          
# newDatabaseName = 'LongTail' 
# charSet = 'utf8mb4'     
# cusrorType = pymysql.cursors.DictCursor

# with open ('muestraurls.csv', 'r') as read_obj:
#     csv_reader = reader(read_obj)
#     for row in csv_reader:
#         word = row[0]
#         print(word)
#         frec = int(row[1])
#         db = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword, database=newDatabaseName, charset=charSet, cursorclass=cusrorType)
#         cursor = db.cursor()
#         cursor.execute("SELECT id_Key, domain, url_codf FROM LongTail.LongTailTable4 WHERE domain LIKE %s LIMIT 0, %s",(word,frec))
#         # myresult = cursor.fetchall()
#         # print(myresult[0])
        
#         cursor.execute("INSERT INTO ParseContent (idbefore, domain, urls) SELECT id_Key, domain, url_codf FROM LongTail.LongTailTable4 WHERE domain LIKE %s LIMIT 0, %s",(word,frec))
#         db.commit()
        
# db.close()
#CAMBIAR CARACTER DE UN REGISTRO EXISTENTE#############################################################################

# i = 1284
# inicio = default_timer()
# while i <= 80000:
#     print(i)
#     cursor.execute("SELECT urls FROM LongTail.ParseContent WHERE id_Key= %s",(i))
#     myresult = cursor.fetchone()
#     listOfValues = myresult.values() #convertir valores de diccionario a lista
#     listOfValues = list(listOfValues)
#     listOfValues = str(listOfValues[0])
        
#     substring1 = "%25"
       
#     if substring1 in listOfValues:
#         result = listOfValues.replace('%25', '%')
#         #print(result)
#     else:
#         result = listOfValues
#     print(result)
#     cursor.execute("UPDATE LongTail.ParseContent SET urls = %s WHERE id_Key= %s",(result,i))
#     cursor.execute("SELECT * FROM LongTail.ParseContent WHERE id_Key=1")
#     myresult = cursor.fetchone()
#     db.commit()
#     i += 1
# db.close()
# fin = default_timer()
# print("Programa terminado", fin-inicio)  

  
import pymysql
import re
from timeit import default_timer
import pandas as pd
from csv import reader
####################################################################################################################
####################################################################################################################
####################################################################################################################
# MODIFY PRYMARY KEY ################################################################################
# cursor.execute("ALTER TABLE LongTail.ParseContent ADD id_Key int UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")
# ALTER TABLE members DROP ID;
# ALTER TABLE members AUTO_INCREMENT = 1;
# ALTER TABLE members ADD ID int UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST
# db.commit()
# db.close()
####################################################################################################################
####################################################################################################################
####################################################################################################################
# MODIFY PRYMARY KEY ################################################################################
conda activate from bs4 import BeautifulSoup
import requests

databaseServerIP = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'  
databaseUserName = 'aforero'      
databaseUserPassword = 'wz5LeyV4TkDGq7<r'          
newDatabaseName = 'LongTail' 
charSet = 'utf8mb4'     
cusrorType = pymysql.cursors.DictCursor
db = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword, database=newDatabaseName, charset=charSet, cursorclass=cusrorType)
cursor = db.cursor()

i = 7567
inicio = default_timer()
while i <= 10500:
    print(i)
    inicio2 = default_timer()
    cursor.execute("SELECT urls FROM LongTail.ParseContent WHERE id_Key= %s",(i))
    myresult = cursor.fetchone()
    listOfValues = myresult.values() #convertir valores de diccionario a lista
    listOfValues = list(listOfValues)
    listOfValues = str(listOfValues[0])
    #print(listOfValues)
    fin1 = default_timer()
    print("URL obtenida: ", fin1 - inicio2)
    try:          
        url = listOfValues

        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        fin2 = default_timer()
        print("html obtenido: ", fin2 - fin1)

        title = soup.find('title')
        #print("title: ",title.string)
        title = str(title.string)
        h1 = soup.find('h1')
                #print("h1: ",h1.string)
        h1 = str(h1.string)
        meta = soup.find('meta')
                #print("meta: ",meta.string)
        meta = str(meta.string)
        images = []
        for img in soup.findAll('img'):
            images.append(img.get('src'))
                #print(images)
        images = str(images)
        text = []
        for idx, item in enumerate(soup.find_all("p")):
            text.append(item.text)
        text = str(text)
        #print(text)
        
        fin3 = default_timer()
        print("parseado: ", fin3 - fin2)    

        cursor.execute("UPDATE LongTail.ParseContent SET title = %s WHERE id_Key= %s",(title,i))
        cursor.execute("UPDATE LongTail.ParseContent SET h1 = %s WHERE id_Key= %s",(h1,i))
        cursor.execute("UPDATE LongTail.ParseContent SET meta = %s WHERE id_Key= %s",(meta,i))
        cursor.execute("UPDATE LongTail.ParseContent SET url_imagenes = %s WHERE id_Key= %s",(images,i))
        cursor.execute("UPDATE LongTail.ParseContent SET parrafos = %s WHERE id_Key= %s",(text,i))
                
        db.commit()
        fin4 = default_timer()
        print("Data cargada: ", fin4 - fin3)
        i += 1
        
    except Exception as error:
        errorDescr = error
        ReporteDeErrores = open("ReporteDeErroresparseando.csv", "a")
        ReporteDeErrores.write("i,error \n")
        ErrorList = []
        ErrorList.append(str(i))
        ErrorList.append(str(listOfValues))
        ErrorList.append(str(errorDescr))
        ReporteDeErrores.write("|".join(ErrorList))
        ReporteDeErrores.close
        i += 1
    
db.close()
fin = default_timer()
print("Programa terminado", fin-inicio)

