import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import  Options
import requests

distribuidorConteudo = []
empresa = []
telefone = []
email = []

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\xampp\htdocs\diretorio\Web-Scraping\ScrapingSindipecas\chromedriver.exe')
#driver = webdriver.Chrome(executable_path=r'C:\xampp\htdocs\diretorio\Web-Scraping\ScrapingSindipecas\chromedriver.exe')
url = (f'https://www.sindipecas.org.br/associados_e_produtos/list.php?tipo=empresa&busca=&btn_submit=Filtrar&merc1=merc1&merc2=merc2&merc3=merc3&merc4=merc4')
driver.get(url)
time.sleep(2)

page = 1
qtdPage = 9

while page != qtdPage + 1:

    url = (f'https://www.sindipecas.org.br/associados_e_produtos/list.php?pagina={page}')
    driver.get(url)
    page += 1

    time.sleep(3)
    empNum = 1
    QtdEmpPage = 10

    if page == 9:
        QtdEmpPage = 6
    
    while empNum != QtdEmpPage + 1:
        element = driver.find_element_by_xpath(f"//div[{empNum + 1}][contains(@class, 'associado')]")  
        empNum += 1

        html_content = element.get_attribute("outerHTML")
        soup = BeautifulSoup(html_content, "html.parser")

        for conteudoTag in soup.find_all("a", limit=3):
            conteudoTag = conteudoTag.get_text()
            conteudoTag = conteudoTag.strip()
            distribuidorConteudo.append(conteudoTag)

            if len(distribuidorConteudo) == 1:
                empresa.append(distribuidorConteudo[0])

            if len(distribuidorConteudo) == 2:
                telefone.append(distribuidorConteudo[1])

            if len(distribuidorConteudo) == 3:
                email.append(distribuidorConteudo[2])

        distribuidorConteudo.clear()

driver.quit()

#importe o pandas para converter a lista em uma planilha

import pandas as pd

df = pd.DataFrame(columns=['Empresa'])

df['Empresa']=empresa
df['Telefone']=telefone
df['E-mail']=email

#writing to Excel

datatoexcel = pd.ExcelWriter('C:/xampp/htdocs/diretorio/Web-Scraping/Relatorios/Scraping-SINDIPECAS.xlsx')

# write DataFrame to excel

df.to_excel(datatoexcel)

# save the excel

datatoexcel.save()

print('DataFrame is written to Excel File successfully.')
