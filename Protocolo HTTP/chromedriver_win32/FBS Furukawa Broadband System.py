import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import  Options
import json
import urllib.request

listaProdutos = []
listaObs = []
cont = 0

while cont != 1:
    cont +=1
    
    url = (f'https://www.furukawalatam.com/pt-br/catalogo-de-produtos-categoria/FBS?page={cont}')

# Pegar conteudo HTML a partir da URL

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=r'C:\xampp\htdocs\diretorio\Web-Scraping\Protocolo HTTP\chromedriver_win32\chromedriver.exe')
    driver.get(url)

    time.sleep(10)

    element = driver.find_element_by_xpath("//div[@class='container d-flex mt-2']")
    #driver.find_element_by_xpath("//nav[@class='d-flex justify-content-center mt-5']//ul[@class='pagination']//li[@class='page-item']//a[class='page-link active']").click()
    html_content = element.get_attribute("outerHTML")


    #Parsear o conteudo HTML  - BeautifulSoup

    soup = BeautifulSoup(html_content, "html.parser")
    descricao = soup.find_all('p', attrs={'product-name title break-all'})
    observacao = soup.find_all('p', attrs={'pb-3 fillterBy'}) 

    for descri in descricao:
        descricao = descri.get_text()
        listaProdutos.append(descricao)
        
    for obser in observacao:
        obs = obser.get_text()
        listaObs.append(obs)
        
    driver.quit()
    
import pandas as pd

data = {
    1: listaProdutos,
    2: listaObs
}

lista = pd.DataFrame(data = {
    "Descrição": listaProdutos,
    "Especificação": listaObs
})

print(lista)
