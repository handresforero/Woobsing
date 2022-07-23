#conda activate UTEL
#cd D:\Woobsing\UTEL

from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
from collections import Counter
from string import punctuation
import pandas as pd
from timeit import default_timer

df = pd.read_excel('BDConsolidadoLinksServer - copia.xlsx')
mylist = df['url'].tolist()

i = 1

for u in mylist:
    inicio1 = default_timer()
    print(i)
    
    html = urlopen(u).read()
    soup = BeautifulSoup(html)

    #list_tags = soup.find_all(class_="thim-course-content") #Extrae todo el código html
    #print(list_tags)

    text = soup.body.find('div', attrs={'class' : 'thim-course-content'}).text #extrae todo el texto del elemento

    strips = list(text.split())

    c = Counter((x.rstrip(punctuation).lower() for y in strips for x in y.split()))
    print(c)
    
    df1 = pd.DataFrame.from_dict(c, orient='index')#.reset_index()
    df1[''] = u
    df1.to_csv('existing_dataServer_UtelV3.csv', mode='a')
    # with pd.ExcelWriter('output.xlsx',  #save in diferentes sheets
    #                 mode='a') as writer: 
    #     df1.to_excel(writer)
    i += 1
    fin1 = default_timer()
    print("t. ejec:", fin1 - inicio1)
    
fin = default_timer()
print("t. ejec:", fin - inicio)