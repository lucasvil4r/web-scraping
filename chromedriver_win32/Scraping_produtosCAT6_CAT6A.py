import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver

#def obterCodigoFonte(url):
#    chrome_options = webdriver.ChromeOptions()
#    chrome_options.add_argument('--headless')
#    driver = webdriver.Chrome(executable_path=r'C:\Users\DEPOSITO\Clone repositorio\Web Scraping\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)
#    driver.get(url)
#    return driver.page_source

#def processarCodigoFonte(cf):
#    soup = BeautifulSoup(cf, 'html.parser')
#    getValueFromDiv = soup.find('p', class_='product-name title break-all')
#    return getValueFromDiv.text
#
#url = 'https://www.furukawalatam.com/pt-br/catalogo-de-produtos-categoria/FCS/'
#codigoFonte = obterCodigoFonte(url)
#print(processarCodigoFonte(codigoFonte))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=r'C:\caminho do chromeDriver...', chrome_options=chrome_options)
driver.get
url = 'https://www.furukawalatam.com/pt-br/catalogo-de-produtos-categoria/FCS/'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
print(soup.prettify)
