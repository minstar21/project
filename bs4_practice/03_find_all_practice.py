from bs4 import BeautifulSoup

f = open("02_ul_li.html")
bsobj = BeautifulSoup(f.read(),"html.parser")
print(bsobj)
ul = bsobj.find("ul")
print(ul.text)
li = ul.find("li") #결과값 한 줄만 나옴
print(li)
lis = ul.find_all("li") #결과값 전체
print(lis)

for i in lis:
    print(i)