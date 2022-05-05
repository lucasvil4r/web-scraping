import urllib.request
from bs4 import BeautifulSoup


url = 'https://www.furukawalatam.com/pt-br/catalogo-de-produtos-categoria/FCS/'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
list_prod = soup.find_all('p', attrs={'class': 'product-name title break-all'})
print(soup.prettify())

#for prod in list_prod:
#    print(prod.get_text())
