# import pandas as pd                        
# from pytrends.request import TrendReq
# pytrend = TrendReq()
# pytrend.build_payload(kw_list=[‘Taylor Swift’])
# # Interest by Region
# df = pytrend.interest_by_region()
# df.head(10)
# df.reset_index().plot(x=’geoName’, y=’Taylor Swift’, figsize=(120, 10), kind =’bar’


from pytrends.request import TrendReq

file = open('listadoDePalabrasGoogleTrends.csv', encoding='utf-8')
kw_list = file.read().splitlines()
i = 0

while i <= 2688:
    print(kw_list[i+1])
    res = [kw_list[0], kw_list[i+1], kw_list[i+2], kw_list[i+3], kw_list[i+4]]
    
    pytrends = TrendReq(hl='es-MX', tz=360)
    pytrends.build_payload(res, cat=0, timeframe='2021-01-01 2022-02-01', geo='MX', gprop='')
    gt_o3_ytd1 = pytrends.interest_over_time()
    mean = gt_o3_ytd1.mean()
    #print(mean)          
    the_file = open("kw_list_GoogleTrendsV2.csv", "a")
    #the_file.write("i,urlPagina,urlReal,domain,urls \n")  
    the_file.write(str(mean))
    the_file.close()    
    i += 4