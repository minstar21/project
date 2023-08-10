from bs4 import BeautifulSoup

f = open("tag_practice.html")
print()

bsobj = BeautifulSoup(f.read(), "html.parser")
print(bsobj)

h1 = bsobj.find("h1")
p = bsobj.find("p")
h2 = bsobj.find('h2')
print(h1)
print(p.text)
print(h2)