import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.efurukawa.com/br/c?Nrpp=437&ajaxPage=false'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
list_prod = soup.find_all('h2', attrs={'product-name'})
list_code = soup.find_all('span', attrs={'product-code'})

for prod in list_prod:
    print(prod.get_text())

for code in list_code:
    print(code.get_text())