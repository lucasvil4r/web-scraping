import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.efurukawa.com/br/c/todos-os-produtos?Nrpp=437&ajaxPage=false'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

#list_code = soup.find_all('span', attrs={'product-code'})
#list_prod = soup.find_all('h2', attrs={'class': 'product-name'})

list_prod = soup.find_all('h2', attrs={'class': 'product-name'})
list_code = soup.find_all('span', attrs={'product-code'})
print(f'{list_prod} \ {list_code}')
