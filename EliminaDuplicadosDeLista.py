import pandas as pd
import numpy as np
from timeit import default_timer
from collections import OrderedDict
import csv


#################################################################################################################
#################################################################################################################
#################################################################################################################
#ELIMINATE DUPLICATES ###########################################################################################

# df = pd.read_excel('Elimina palabas.xlsx')
# mylist1 = df['Nivel 4'].tolist()
# #prueba = (mylist1[0])
# #print(type(prueba))

# # def unique_list(l):
# #     ulist = []
# #     [ulist.append(x) for x in l if x not in ulist]
# #     return ulist

# # a=str(prueba)
# # a=a.replace(",", " ")
# # a=' '.join(unique_list(a.split()))
# # a=a.replace(" ", ",")
# # print(a)

# i=1
# the_file = open("arreglos.csv", "a")
# for index, row in df.iterrows():
#     print(i)
#     letter_list1 = row['Nivel 4'].split(",")
    
#     def unique_list(l):
#         ulist = []
#         [ulist.append(x) for x in l if x not in ulist]
#         return ulist

#     a=str(letter_list1)
#     a=a.replace(",", " ")
#     a=' '.join(unique_list(a.split()))
#     a=a.replace(" ", ",")
#     the_list = []
#     the_list.append(str(i))
#     the_list.append(str(a))
#     the_list.append("\n")
#     the_file.write(",".join(the_list))
#     the_file.close
#     i += 1
#################################################################################################################    


df = pd.read_excel('Elimina palabas.xlsx')
mylist1 = df['Categorías madre'].tolist()
mylist2 = df['Nivel 4'].tolist()
#prueba = (mylist1[0])
#print(type(prueba))

# def unique_list(l):
#     ulist = []
#     [ulist.append(x) for x in l if x not in ulist]
#     return ulist

# a=str(prueba)
# a=a.replace(",", " ")
# a=' '.join(unique_list(a.split()))
# a=a.replace(" ", ",")
# print(a)

i=1
the_file = open("arreglos.csv", "a")
for index, row in df.iterrows():
    print(i)
        
    letter_list1 = row['Categorías madre'].split(",")
    letter_list2 = row['Nivel 4'].split(",")
    
    list3 = [elt for elt in letter_list2 if elt not in letter_list1]    
    
    the_list = []
    the_list.append(str(i))
    the_list.append(str(list3))
    the_list.append("\n")
    the_file.write(",".join(the_list))
    the_file.close
    i += 1