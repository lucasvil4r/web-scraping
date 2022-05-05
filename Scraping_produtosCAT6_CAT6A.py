import urllib.request
import requests
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

url = 'https://www.furukawalatam.com/pt-br/catalogo-de-produtos-categoria/FCS/categoria/gigalan---cat-6a:gigalan---cat-6'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
list_prod = soup.find_all('p', attrs={'class': 'product-name title break-all'})
print(soup.prettify())

#for prod in list_prod:
#    print(prod.get_text())
