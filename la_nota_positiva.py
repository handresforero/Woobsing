# #conda create -n la_nota_positiva python=3.9
# #conda activate la_nota_positiva
# #cd D:\Woobsing\LaNotaPositiva

# from requests_html import HTML

# with open('view-source_https___es.wikipedia.org_wiki_Python.html', encoding="utf8") as html_file:
#     source = html_file.read()
#     html = HTML(html=source)
# #print(html.html)
# #print(html.text)
# article = html.find('div.contetn', first=True)
# print(article.text)

# ####################################################################################################################
# import requests
# from bs4 import BeautifulSoup
# import bs4

# response = requests.get(
# 	url="https://es.wikipedia.org/wiki/Python",
# )
# soup = BeautifulSoup(response.content, 'html.parser')

# title = soup.find(id="firstHeading")
# print("Título: ",title.string)



# title2 = soup.find(class_ ="mw-parser-output")
# print("Título: ",title2.string)
#/html/body/div[3]/div[3]/div[5]/div[1]/p[1]
#<div class="mw-parser-output">

# url="https://es.wikipedia.org/wiki/Python"
# import metadata_parser
# page = metadata_parser.MetadataParser(url)
# print(page.metadata)
# print(page.get_metadatas('title'))


# from bs4 import BeautifulSoup
# import requests
# import csv

# source = requests.get('https://es.wikipedia.org/wiki/Python').text

# soup = BeautifulSoup(source, 'lxml')

# csv_file = open('cms_scrape.csv', 'w')

# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['headline', 'summary', 'video_link'])

# for article in soup.find_all('article'):
#     headline = article.h2.a.text
#     print(headline)

#     summary = article.find('div', class_='entry-content').p.text
#     print(summary)

#     try:
#         vid_src = article.find('iframe', class_='youtube-player')['src']

#         vid_id = vid_src.split('/')[4]
#         vid_id = vid_id.split('?')[0]

#         yt_link = f'https://youtube.com/watch?v={vid_id}'
#     except Exception as e:
#         yt_link = None

#     print(yt_link)

#     print()

#     csv_writer.writerow([headline, summary, yt_link])

# csv_file.close()



##################################################################################################################
# from bs4 import BeautifulSoup
# import requests

# res = requests.get("https://es.wikipedia.org/wiki/Python")
# soup = BeautifulSoup(res.text, 'html.parser')
# for item in soup.find_all("p"):
#     if item.text.startswith("Historia"):break
#     print(item.text)
#####################################################################################################################
#####################################################################################################################
#      WIKIPEDIA      ###############################################################################################
from bs4 import BeautifulSoup
import requests

url = "https://es.wikipedia.org/wiki/Python"

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

title = soup.find('title')
#print("title: ",title.string)
h1 = soup.find('h1')
#print("h1: ",h1.string)
meta = soup.find('meta')
#print("meta: ",meta.string)
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))
#print(images)
text = []
for idx, item in enumerate(soup.find_all("p")):
    text.append(item.text)
print(text)

# textos = soup.find_all('p')
# print(textos)

# for soupContent in soup.find_all('p'):
#      print(soupContent.text)

# VALID_TAGS = ['div', 'p']
# for tag in soup.findAll('p'):
#     if tag.name not in VALID_TAGS:
#         tag.replaceWith(tag.renderContents())

# print(soup.renderContents())


# h1 = soup.find(id="firstHeading")
# #print("H1: ",h1.string)

# for idx, item in enumerate(soup.find_all("p")):
#     if idx == 0:
#         break
# #print("Meta: "item.text)

# text = soup.body.find('div', attrs={'class' : 'mw-parser-output'}).text
# #print(text)

# import wikipedia as wp
# wp_page = wp.page(url)
# list_img_urls = wp_page.images
# # #print(list_img_urls)

