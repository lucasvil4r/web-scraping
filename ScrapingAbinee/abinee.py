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

distribuidorConteudo = []
empresa = []
representante = []
cargoRepresentante = []
endereco = []
CepCidade = []
contato = []
produtos = []
numCliente = []

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\xampp\htdocs\diretorio\Web-Scraping\ScrapingAbinee\chromedriver.exe')

qtdPage = 200
page = 1

while page != qtdPage:

    url = (f'http://www.abinee.org.br/abinee/associa/filiados/{page}.htm')

    response = requests.get(url)
    retorno = response.status_code

    if retorno != 404:

        driver.get(url)

        time.sleep(2)

        element = driver.find_element_by_xpath("//div[@class='conteudo_geral']")

        html_content = element.get_attribute("outerHTML")
        soup = BeautifulSoup(html_content, "html.parser")

        for nomeEmpresa in soup.find('h1', 'titulo'):
            nomeEmpresa = nomeEmpresa.get_text()
            nomeEmpresa = nomeEmpresa.strip()
            empresa.append(nomeEmpresa)

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
                CepCidade.append(distribuidorConteudo[2])
            if len(distribuidorConteudo) == 4:
                contato.append(distribuidorConteudo[3])
            if len(distribuidorConteudo) > 4:
                produtos.append(distribuidorConteudo[indice])

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
df['Cargo Representante']=cargoRepresentante
df['Endereço']=endereco
df['Cep/Cidade']=CepCidade
df['Contato']=contato
df['Cliente Nº']=numCliente

print(df)

#writing to Excel

datatoexcel = pd.ExcelWriter('C:/xampp/htdocs/diretorio/Web-Scraping/Relatorios/Scraping-ABINEE.xlsx')

# write DataFrame to excel

df.to_excel(datatoexcel)

# save the excel

datatoexcel.save()

print('DataFrame is written to Excel File successfully.')
