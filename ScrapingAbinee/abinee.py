import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import  Options
import requests

distribuidorConteudo = []
empresa = []
representante = []
cargoRepresentante = []
endereco = []
cep = []
contato = []
produtos = []
numCliente = []

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\xampp\htdocs\diretorio\Web-Scraping\ScrapingAbinee\chromedriver.exe')

page = 1
qtdPage = 5

while page != qtdPage:

    url = (f'http://www.abinee.org.br/abinee/associa/filiados/{page}.htm')

    response = requests.get(url, timeout=30)
    retorno = response.status_code
    
    if retorno != 404:

        driver.get(url)

        time.sleep(5)

        element = driver.find_element_by_xpath("//div[@class='conteudo_geral']")

        html_content = element.get_attribute("outerHTML")
        soup = BeautifulSoup(html_content, "html.parser")

        for nomeEmpresa in soup.find('h1', 'titulo'):
            nomeEmpresa = nomeEmpresa.get_text()
            nomeEmpresa = nomeEmpresa.strip()
            empresa.append(nomeEmpresa)

            qtdEmpresa = len(empresa) - 1

        for nomeRepresentante in soup.find('strong'):
            nomeRepresentante = nomeRepresentante.get_text()
            nomeRepresentante = nomeRepresentante.strip()
            representante.append(nomeRepresentante)

        indice = -1

        for conteudoTag in soup.find_all("p"):
            conteudoTag = conteudoTag.get_text()
            conteudoTag = conteudoTag.strip()
            distribuidorConteudo.append(conteudoTag)

            if len(distribuidorConteudo) == 1:
                excluiNome = distribuidorConteudo[0]
                excluiNome = excluiNome.replace(nomeRepresentante, '')
                cargoRepresentante.append(excluiNome)

            if len(distribuidorConteudo) == 2:
                endereco.append(distribuidorConteudo[1])

            if len(distribuidorConteudo) == 3:
                cep.append(distribuidorConteudo[2])

            if len(distribuidorConteudo) == 4:
                contato.append(distribuidorConteudo[3])

            if len(distribuidorConteudo) == 5:
                produtos.append(distribuidorConteudo[4])

            if len(distribuidorConteudo) > 5:
                recebeProduto = distribuidorConteudo[indice]
                produtos[qtdEmpresa] = produtos[qtdEmpresa]+" - "+ recebeProduto

        distribuidorConteudo.clear()
        numCliente.append(page)
        page +=1
        indice +=1
    else:
        page +=1

driver.quit()

#importe o pandas para converter a lista em uma planilha

import pandas as pd

df = pd.DataFrame(columns=['Empresa'])

df['Empresa']=empresa
df['Representante']=representante
df['Cargo representante']=cargoRepresentante
df['Endereço']=endereco
df['CEP']=cep
df['Contato']=contato
df['Produtos relacionados']=produtos
df['Filiado Nº']=numCliente

print(df)

#writing to Excel

datatoexcel = pd.ExcelWriter('C:/xampp/htdocs/diretorio/Web-Scraping/Relatorios/Scraping-ABINEE.xlsx')

# write DataFrame to excel

df.to_excel(datatoexcel)

# save the excel

datatoexcel.save()

print('DataFrame is written to Excel File successfully.')
