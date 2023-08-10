import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
def crawl(code):
    url = f"https://finance.naver.com/item/main.naver?code={code}"
    res = requests.get(url)
    bsobj = BeautifulSoup(res.text, 'html.parser')

    div_today = bsobj.find("div", {"class": "today"})
    em = div_today.find("em")
    price = em.find('span').text

    h_company = bsobj.find("div", {"class":"h_company"})
    name = h_company.a.text
    #print(h_company.a.text)
    div_description = h_company.find("div", {"class": "description"})
    code = div_description.span.text
    #print(code)

    table_no_info = bsobj.find('table', {'class':"no_info"})
    #print(table_no_info)
    tds = table_no_info.tr.find_all('td')
    volume = tds[2].find("span", {"class": "blind"}).text
    #print(volume.text)

    dic = {"price": price,"code": code, "name": name,"volume": volume}
    return dic

codes = ["001230","005930", "051910"]
#dic = crawl("001230")
#print(dic)

r = []
for code in codes:
    dic = crawl(code)
    r.append(dic)
print(r)

df = pd.DataFrame(r)
#df.to_excel("prices.xlsx")
print(df)