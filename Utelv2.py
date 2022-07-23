#conda create -n UTEL python=3.9
#conda activate UTEL
#cd D:\Woobsing\UTEL

import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
import csv
import openpyxl
from pathlib import Path
import pandas as pd
from timeit import default_timer

inicio = default_timer()
    
#$$$$$$$$$$$$$$$$$$$$$$$$ SIRVE $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$ SIRVE $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$ SIRVE $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# r = requests.get("https://x.utel.edu.mx/cursos/caxos/gestion-integral-de-destinos-turisticos/")

# soup = BeautifulSoup(r.content)

# text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))

# c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))

# df = pd.DataFrame.from_dict(c, orient='index')#.reset_index()

###################################################################################################################
###################################################################################################################
###################################################################################################################
###################################################################################################################
# sirve para convertir los datos en dataframe
# sirve para convertir los datos en dataframe
# sirve para convertir los datos en dataframe
#bd_file = pd.read_excel('BDConsolidadoLinks - copia.xlsx')
# #mylist = df['url'].tolist()
#df1 = pd.DataFrame(bd_file) # sirve para convertir los datos en dataframe
#print(df1)

df = pd.read_excel('BDConsolidadoLinks - copia.xlsx')
mylist = df['url'].tolist()

for u in mylist:
    r = requests.get(u)
    soup = BeautifulSoup(r.content)
    text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
    c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
    df1 = pd.DataFrame.from_dict(c, orient='index')#.reset_index()
    df1[''] = u
    df1.to_csv('existing_data2.csv', mode='a')
    # with pd.ExcelWriter('output.xlsx',  #save in diferentes sheets
    #                 mode='a') as writer: 
    #     df1.to_excel(writer)
    
fin = default_timer()
print("t. ejec:", fin - inicio)