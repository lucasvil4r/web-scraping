import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import  Options
import json
import urllib.request

cont = 0

while cont != 1:
    cont +=1
    
    url = (f'https://www.furukawalatam.com/pt-br/catalogo-de-produtos-categoria/FIS?page={cont}')

# Pegar conteudo HTML a partir da URL

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=r'C:\xampp\htdocs\diretorio\Web-Scraping\Protocolo HTTP\chromedriver_win32\chromedriver.exe')
    driver.get(url)

    time.sleep(15)

    element = driver.find_element_by_xpath("//div[@class='container d-flex mt-2']")
    #driver.find_element_by_xpath("//nav[@class='d-flex justify-content-center mt-5']//ul[@class='pagination']//li[@class='page-item']//a[class='page-link active']").click()
    html_content = element.get_attribute("outerHTML")


    #Parsear o conteudo HTML  - BeautifulSoup

    soup = BeautifulSoup(html_content, "html.parser")
    descricao = soup.find_all('p', attrs={'product-name title break-all'})
    descricao = soup.find_all('p', attrs={'pb-3 fillterBy'}) 

    for prod in descricao:
        descricao = prod.get_text()
        print(descricao)   

    driver.quit()
    