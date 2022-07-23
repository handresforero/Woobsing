import pymysql
import re
from timeit import default_timer

databaseServerIP = 'baselongtailcontenidos.cmxlnwygo8jr.us-east-2.rds.amazonaws.com'  
databaseUserName = 'aforero'      
databaseUserPassword = 'wz5LeyV4TkDGq7<r'          
newDatabaseName = 'LongTail' 
charSet = 'utf8mb4'     
cusrorType = pymysql.cursors.DictCursor

db = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword, database=newDatabaseName, charset=charSet, cursorclass=cusrorType)
cursor = db.cursor()        