import pymysql
import pywebio
from pywebio.input import input, TEXT 
from pywebio.output import put_text, put_html, put_markdown, put_table
from pywebio import start_server
import argparse
import pandas as pd

def bmi():
    url = input("Ingrese la palabra a buscar：", type=TEXT)
    word = ("%"+url+"%")
    
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
        #cursor.execute("SELECT urlPagina, domain, urls LOCATE %s,urlPagina FROM LongTail.LongTailTable4 WHERE locate %s,urlPagina>0",(i,i))
    #cursor.execute("SELECT urlPagina, domain, urls FROM LongTail.LongTailTable4 WHERE urlPagina LIKE '%noticias%'")
    cursor.execute("SELECT urlPagina, domain, urls FROM LongTail.LongTailTable4 WHERE urlPagina LIKE %s",(word))
    myresult = cursor.fetchall()   

    db.close()
    
    df1 =pd.DataFrame(myresult)
    df2= df1.iloc[:, [1]]
    df3= df1.iloc[:, [2]]
          
    #tabla_url = df1.pivot_table(columns=[' urls '], aggfunc='size')    

    for common in df1:
                
        #put_markdown('# **Resultados**')
        #put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
        #put_html('<br><br>')
        
        put_markdown('# **Resultados de la búsqueda**').style('color: red; font-size: 30px')
        put_text('Powered by Woobsing | Los siguientes son datos obtenidos de la base Elnoti').style('color: grey; font-size: 10px')
        #put_html('<br>Los siguientes son datos obtenidos de la base Elnoti<br>')        
        put_text('Keyword buscada:', url)
            
            
        #put_markdown('Your BMI: `%.1f`. Category: `%s`' % (BMI, status))
        put_html('<hr>')
        put_table([
        #['Dominio', 'URL'],
        [df2,df3],
        ])

        break

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    
    start_server(bmi, port=args.port)
    #pywebio.start_server(bmi, port=80)