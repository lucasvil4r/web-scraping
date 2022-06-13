import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import  Options
import requests

#Códigos de Status
#A primeira coisa que podemos fazer é verificar o código de status. Os códigos HTTP variam de 1XX a 5XX. Os códigos de status comuns que você provavelmente viu são 200, 404 e 500.
#Aqui está uma visão geral rápida do que cada código de status significa:
#1XX - Informação
#2XX - Sucesso
#3XX - Redirecionar
#4XX - Erro de cliente (você cometeu um erro)
#5XX - Erro de servidor (eles cometeram um erro)

qtdPage = 3
page = 2

while page != qtdPage:

    url = (f'http://www.abinee.org.br/abinee/associa/filiados/{page}.htm')

    response = requests.get(url)
    retorno = response.status_code

    if retorno != 404:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\xampp\htdocs\diretorio\Web-Scraping\ScrapingAbinee\chromedriver.exe')

        driver.get(url)

        time.sleep(2)

        element = driver.find_element_by_xpath("//div[@class='conteudo_geral']")

        html_content = element.get_attribute("outerHTML")
        soup = BeautifulSoup(html_content, "html.parser")

        nomeEmpresa = soup.find('h1', attrs={'titulo'})
        print(nomeEmpresa)

        for conteudoTag in soup.findAll("p", limit=4):
            conteudoTag = conteudoTag.get_text()
            conteudoTag = conteudoTag.replace("\t", " ")
            conteudoTag = conteudoTag.replace("\n", " ")
            conteudoTag = conteudoTag.replace("\r", "")
            conteudoTag = conteudoTag.replace(",", ".")
            conteudoTag = conteudoTag.strip()
            print(conteudoTag)

        page +=1
        driver.quit()
    else:
        page +=1
