  
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import os 
import pandas as pd

columns = ['Name','Branch','Roll No','Year','City','State']

branches = ['CSE','ECE','EE','CHE','ME','CE','AR','MS','CSE-DD','ECE-DD']

url = "http://covidinfonith.herokuapp.com/copy-post-info?branch=%s&year=%s&page=%s"

listi = []

for year in range(1,5):
    for branch in branches:
            for page in range(1,20):
                req = Request(url %(branch,str(year),str(page)), headers={'User-Agent': 'Mozilla/5.0'})
                web_byte = urlopen(req).read()

                webpage = web_byte.decode('utf-8')

                page_soup = soup(webpage,"html.parser")

                cont = page_soup.find_all('div',class_ ="alert alert-danger")

                try :
                    print(cont[0])
                    break
                except IndexError:
                    pass

                cont = page_soup.find_all('li',attrs={"style":"list-style-type: none ;"})

                big = []
                for contain in cont:
                    h4_cont = contain.find_all('h4')
                    h = [h4_cont[i].text for i in range(6) ]
                    big.append(h)

                for bi in big:
                    listi.append(bi)
            print(big)
df = pd.DataFrame(listi,columns=columns)
df = df.replace({'State = ': '','District =':''}, regex=True)
df.to_csv("./dataset/All/all.csv",index=False)
print(df)

