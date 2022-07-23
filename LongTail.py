#conda create -n LongTail python=3.9
#conda activate LongTail
#cd D:\Woobsing\LongTail

#pip install python-csv

from email.policy import default
import pymysql
import pymysql.cursors
import csv 


#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#CREATE A DATABASE MYSQL#############################################################################################

# # Create a connection object
# databaseServerIP = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'  # IP address of the MySQL database server
# databaseUserName = 'aforero'      # User name of the database server
# databaseUserPassword = 'wz5LeyV4TkDGq7<r'          # Password for the database user
# newDatabaseName = 'LongTail' # Name of the database that is to be created
# charSet = 'utf8mb4'     # Character set
# cusrorType = pymysql.cursors.DictCursor

# connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword, charset=charSet,cursorclass=cusrorType)

# try:
#     # Create a cursor object
#     cursorInsatnce = connectionInstance.cursor()                      

#     # SQL Statement to create a database
#     sqlStatement = 'CREATE DATABASE '+newDatabaseName  

#     # Execute the create database SQL statment through the cursor instance
#     cursorInsatnce.execute(sqlStatement) 

#     # SQL query string
#     sqlQuery = 'SHOW DATABASES' 

#     # Execute the sqlQuery
#     cursorInsatnce.execute(sqlQuery) 

#     #Fetch all the rows
#     databaseList = cursorInsatnce.fetchall() 

#     for datatbase in databaseList:
#         print(datatbase) 

# except Exception as e:
#     print("Exeception occured:{}".format(e)) 

# finally:
#     connectionInstance.close()

#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################



#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#CREATE A TABLE MYSQL#############################################################################################
# databaseServerIP = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'  # IP address of the MySQL database server
# databaseUserName = 'aforero'      # User name of the database server
# databaseUserPassword = 'wz5LeyV4TkDGq7<r'          # Password for the database user
# newDatabaseName = 'LongTail' # Name of the database that is to be created
# charSet = 'utf8mb4'     # Character set
# cusrorType = pymysql.cursors.DictCursor

# connectionObject = pymysql.connect(host=databaseServerIP,
#                              user=databaseUserName,
#                              password=databaseUserPassword,
#                              database=newDatabaseName,
#                              charset=charSet,
#                              cursorclass=cusrorType)

# try:              
#     # Create a cursor object
#     cursorObject = connectionObject.cursor()                                     
#     # SQL query string
#     sqlQuery = "CREATE TABLE LongTailTable(id int, urlPagina varchar(2048), urlReal varchar(2048), domain varchar(32), urls varchar(2048))"   
#     # Execute the sqlQuery
#     cursorObject.execute(sqlQuery) 
#     # SQL query string
#     sqlQuery = "show tables"   
#     # Execute the sqlQuery
#     cursorObject.execute(sqlQuery) 
#     #Fetch all the rows
#     rows = cursorObject.fetchall() 
#     for row in rows:
#         print(row)
# except Exception as e:
#     print("Exeception occured:{}".format(e))
# finally:
#     connectionObject.close()

#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################


#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#CREATE VARIABLES AND UPLOAD INFRMATION ONE BY ONE OR MULTIPPLE######################################################

# databaseServerIP = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'  # IP address of the MySQL database server
# databaseUserName = 'aforero'      # User name of the database server
# databaseUserPassword = 'wz5LeyV4TkDGq7<r'          # Password for the database user
# newDatabaseName = 'LongTail' # Name of the database that is to be created
# charSet = 'utf8mb4'     # Character set
# cusrorType = pymysql.cursors.DictCursor

# mydb = pymysql.connect(host=databaseServerIP,
#                              user=databaseUserName,
#                              password=databaseUserPassword,
#                              database=newDatabaseName,
#                              charset=charSet,
#                              cursorclass=cusrorType)
# # mycursor = mydb.cursor()
# # mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# # mycursor.execute("SHOW TABLES")

# # for x in mycursor:
# #   print(x)
# mycursor = mydb.cursor()

# sql = 'INSERT INTO customers (name, address) VALUES (%s, %s)'
# val = ('John', 'Highway 21')
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

# ##############################################################################################################################################################

# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################



#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#CREATE TABLES AND VARIABLES######################################################


# databaseServerIP = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'  # IP address of the MySQL database server
# databaseUserName = 'aforero'      # User name of the database server
# databaseUserPassword = 'wz5LeyV4TkDGq7<r'          # Password for the database user
# newDatabaseName = 'LongTail' # Name of the database that is to be created
# charSet = 'utf8mb4'     # Character set
# cusrorType = pymysql.cursors.DictCursor

# connectionObject = pymysql.connect(host=databaseServerIP,
#                              user=databaseUserName,
#                              password=databaseUserPassword,
#                              database=newDatabaseName,
#                              charset=charSet,
#                              cursorclass=cusrorType)

# try:              
#     #Create a cursor object
#     cursorObject = connectionObject.cursor()                                     
#     #SQL query string
#     sqlQuery = "CREATE TABLE LongTailTable4(id int, urlPagina longtext, urlReal longtext, domain longtext, urls longtext)"   
#     #Execute the sqlQuery
#     cursorObject.execute(sqlQuery) 
#     #SQL query string
#     sqlQuery = "show tables"   
#     #Execute the sqlQuery
#     cursorObject.execute(sqlQuery) 
#     #Fetch all the rows
#     rows = cursorObject.fetchall() 
#     for row in rows:
#         print(row)
# except Exception as e:
#     print("Exeception occured:{}".format(e))
# finally:
#     connectionObject.close()

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################


# databaseServerIP = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'  # IP address of the MySQL database server
# databaseUserName = 'aforero'      # User name of the database server
# databaseUserPassword = 'wz5LeyV4TkDGq7<r'          # Password for the database user
# newDatabaseName = 'LongTail' # Name of the database that is to be created
# charSet = 'utf8mb4'     # Character set
# cusrorType = pymysql.cursors.DictCursor

# mydb = pymysql.connect(host=databaseServerIP,
#                              user=databaseUserName,
#                              password=databaseUserPassword,
#                              database=newDatabaseName,
#                              charset=charSet,
#                              cursorclass=cusrorType)
# # mycursor = mydb.cursor()
# # mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# # mycursor.execute("SHOW TABLES")

# # for x in mycursor:
# #   print(x)
# mycursor = mydb.cursor()

# sql = 'INSERT INTO LongTailTable2 (id, urlPagina) VALUES (%s, %s)'
# val = ('3', 'https://footer.woobsing.co/test.php?laurl=www.google.com/searchQMARKq=merelMASMASANPERSANrlz=1C1LHNE_enCO501CO501ANPERSANoq=merelMASMASANPERSANgl=coANPERSANnum=10')
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################



#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#UPLOAD CSV FILE IN DATABASE######################################################
from timeit import default_timer

inicio = default_timer()

databaseServerIP = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'  # IP address of the MySQL database server
databaseUserName = 'aforero'      # User name of the database server
databaseUserPassword = 'wz5LeyV4TkDGq7<r'          # Password for the database user
newDatabaseName = 'LongTail' # Name of the database that is to be created
charSet = 'utf8mb4'     # Character set
cusrorType = pymysql.cursors.DictCursor


db = pymysql.connect(host=databaseServerIP,
                             user=databaseUserName,
                             password=databaseUserPassword,
                             database=newDatabaseName,
                             charset=charSet,
                             cursorclass=cusrorType)

cursor = db.cursor()

fin1 = default_timer()
print("conexión a BD Amazon:", fin1 - inicio)

# f = csv.reader(open('10a20mil.csv'), delimiter='|')

# fin2 = default_timer()
# print("Abrir BD CSV:", fin2 - fin1)

# sql = 'INSERT INTO LongTailTable4 (id, urlPagina, urlReal, domain, urls) VALUES (%s, %s, %s, %s, %s)'
# next(f)
# i = 2
# for line in f:
#     fin3 = default_timer()    
#     line=[None if cell == '' else cell for cell in line]
#     cursor.execute(sql, line)
#     fin4 = default_timer()
#     print("Carga registro:", i, fin4 - fin3)
#     i += 1


# f = csv.reader(open('20a30mil.csv'), delimiter='|')

# fin2 = default_timer()
# print("Abrir BD CSV:", fin2 - fin1)

# sql = 'INSERT INTO LongTailTable4 (id, urlPagina, urlReal, domain, urls) VALUES (%s, %s, %s, %s, %s)'
# next(f)
# i = 2
# for line in f:
#     fin3 = default_timer()    
#     line=[None if cell == '' else cell for cell in line]
#     cursor.execute(sql, line)
#     fin4 = default_timer()
#     print("Carga registro BD 20a30:", i, fin4 - fin3)
#     i += 1


f = csv.reader(open('30a40mil.csv'), delimiter='|')

fin2 = default_timer()
print("Abrir BD CSV:", fin2 - fin1)

sql = 'INSERT INTO LongTailTable4 (id, urlPagina, urlReal, domain, urls) VALUES (%s, %s, %s, %s, %s)'
next(f)
i = 2
for line in f:
    fin3 = default_timer()    
    line=[None if cell == '' else cell for cell in line]
    cursor.execute(sql, line)
    fin4 = default_timer()
    print("Carga registro BD 30a40:", i, fin4 - fin3)
    i += 1


f = csv.reader(open('40a60mil.csv'), delimiter='|')

fin2 = default_timer()
print("Abrir BD CSV:", fin2 - fin1)

sql = 'INSERT INTO LongTailTable4 (id, urlPagina, urlReal, domain, urls) VALUES (%s, %s, %s, %s, %s)'
next(f)
i = 2
for line in f:
    fin3 = default_timer()    
    line=[None if cell == '' else cell for cell in line]
    cursor.execute(sql, line)
    fin4 = default_timer()
    print("Carga registro BD 40a60:", i, fin4 - fin3)
    i += 1

f = csv.reader(open('60a70mil.csv'), delimiter='|')

fin2 = default_timer()
print("Abrir BD CSV:", fin2 - fin1)

sql = 'INSERT INTO LongTailTable4 (id, urlPagina, urlReal, domain, urls) VALUES (%s, %s, %s, %s, %s)'
next(f)
i = 2
for line in f:
    fin3 = default_timer()    
    line=[None if cell == '' else cell for cell in line]
    cursor.execute(sql, line)
    fin4 = default_timer()
    print("Carga registro BD 60a70:", i, fin4 - fin3)
    i += 1


f = csv.reader(open('70a80mil.csv'), delimiter='|')

fin2 = default_timer()
print("Abrir BD CSV:", fin2 - fin1)

sql = 'INSERT INTO LongTailTable4 (id, urlPagina, urlReal, domain, urls) VALUES (%s, %s, %s, %s, %s)'
next(f)
i = 2
for line in f:
    fin3 = default_timer()    
    line=[None if cell == '' else cell for cell in line]
    cursor.execute(sql, line)
    fin4 = default_timer()
    print("Carga registro BD 70a80:", i, fin4 - fin3)
    i += 1


db.commit()
cursor.close()
db.close()
fin5 = default_timer()
print("Carga registro:", i, fin5 - inicio)
print ("Imported")

#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################























# connection = pymysql.connect(host=databaseServerIP,
#                              user=databaseUserName,
#                              password=databaseUserPassword,
#                              database=newDatabaseName,
#                              charset=charSet,
#                              cursorclass=cusrorType)

# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO 'users' ('email', 'password') VALUES (%s, %s)"
#         cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

#     # connection is not autocommit by default. So you must commit to save your changes.
#     connection.commit()

#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT 'id', 'password' FROM 'users' WHERE 'email'=%s"
#         cursor.execute(sql, ('webmaster@python.org',))
#         result = cursor.fetchone()
#         print(result)

# db = pymysql.connect(host=databaseServerIP,
#                              user=databaseUserName,
#                              password=databaseUserPassword,
#                              database=newDatabaseName,
#                              charset=charSet,
#                              cursorclass=cusrorType)

# cursor = db.cursor()
# f = csv.reader(open('domainschanged8.csv'))
# sql = "INSERT INTO test.table(i,urls) VALUES(%s,%s)"
# next(f)
# for line in f:
#     line=[None if cell == '' else cell for cell in line]
#     cursor.execute(sql, line)

# db.commit()
# cursor.close()
# db.close()
# print ("Imported")




# cursor = connection.cursor()
# #delete_existing_table = 'DROP TABLE IF EXIST URL'
# create_table_query = """CREATE TABLE url(
#     i,
#     urlPagina,
#     urlReal,
#     domain,
#     urls
#     )"""

# try:
#     cursor.execute( delete_existing_table )
#     print("Existing table has been deleted")
#     cursor.execute( create_table_query )
#     print("Table has been created")
# except Exception as e:
#     print("Exception courred: ",e)
    
# connection.close()






# connection = pymysql.connect(host=databaseServerIP,
#                              user=databaseUserName,
#                              password=databaseUserPassword,
#                              database=newDatabaseName,
#                              charset=charSet,
#                              cursorclass=cusrorType)

# try:
#     with connection.cursor() as cursor:
#         sqlQuery = "CREATE TABLE IF NOT EXISTS sdata(Date INT Open DECIMAL(18,4), High DECIMAL(18, 4), Low DECIMAL(18, 4), Close DECIMAL(18, 4))"
#         cursor.esecute(sqlQuery)
# finalyy:
#     connection.close()








# import csv
# import pymysql

# databaseServerIP = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'  # IP address of the MySQL database server
# databaseUserName = 'aforero'      # User name of the database server
# databaseUserPassword = 'wz5LeyV4TkDGq7<r'          # Password for the database user
# newDatabaseName = 'LongTail' # Name of the database that is to be created
# charSet = 'utf8mb4'     # Character set
# cusrorType = pymysql.cursors.DictCursor

# mydb = pymysql.connect(host=databaseServerIP,
#                        user=databaseUserName,
#                        password=databaseUserPassword,
#                        database=newDatabaseName,
#                        charset=charSet,
#                        cursorclass=cusrorType)

# cursor = mydb.cursor()
# csv_data = csv.reader('domainschanged8.csv')

# for row in csv_data:
# 	cursor.execute("INSERT INTO LongTail.LongTailTable(id, urlPagina, urlReal, domain, urls) VALUES(%s, %s, %s, %s, %s)", row)

# mydb.commit()
# cursor.close()
# print("Imported!")








# sql = 'INSERT INTO LongTailTable2 (id, urlPagina) VALUES (%s, %s)'
# val = ('3', 'https://footer.woobsing.co/test.php?laurl=www.google.com/searchQMARKq=merelMASMASANPERSANrlz=1C1LHNE_enCO501CO501ANPERSANoq=merelMASMASANPERSANgl=coANPERSANnum=10')
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")


# databaseServerIP = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'  # IP address of the MySQL database server
# databaseUserName = 'aforero'      # User name of the database server
# databaseUserPassword = 'wz5LeyV4TkDGq7<r'          # Password for the database user
# newDatabaseName = 'LongTail' # Name of the database that is to be created
# charSet = 'utf8mb4'     # Character set
# cusrorType = pymysql.cursors.DictCursor

# mydb = pymysql.connect(host=databaseServerIP,
#                              user=databaseUserName,
#                              password=databaseUserPassword,
#                              database=newDatabaseName,
#                              charset=charSet,
#                              cursorclass=cusrorType)
# # mycursor = mydb.cursor()
# # mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# # mycursor.execute("SHOW TABLES")

# # for x in mycursor:
# #   print(x)
# mycursor = mydb.cursor()

# sql = 'INSERT INTO LongTailTable2 (id, urlPagina, urlReal, domain, urls) VALUES (%s, %s, %s, %s, %s)'
# val = ('22501', 'merel/', 'https://footer.woobsing.co/test.php?laurl=www.google.com/searchQMARKq=merelMASMASANPERSANrlz=1C1LHNE_enCO501CO501ANPERSANoq=merelMASMASANPERSANgl=coANPERSANnum=10', 'woobsing.co', 'https://footer.woobsing.co/test.php?laurl=www.google.com/searchQMARKq=merelMASMASANPERSANrlz=1C1LHNE_enCO501CO501ANPERSANoq=merelMASMASANPERSANgl=coANPERSANnum=10')
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")





