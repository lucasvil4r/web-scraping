import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import  Options

distribuidorConteudo = []
empresaCobaia = []
emailCobaia = []
telefoneCobaia = []
siteCobaia = []
empresa = []
email = []
telefone = []
site = []

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\xampp\htdocs\diretorio\Web-Scraping\ScrapingAbsolarorg\chromedriver.exe')

url = (f'https://www.absolar.org.br/nossos-associados/')
driver.get(url)

time.sleep(5)

element = driver.find_element_by_xpath("//div[@class='row associates-itens']")

qtdEmpresaPage = 693
contadorEmpresa = 1

while contadorEmpresa != qtdEmpresaPage:
    element = driver.find_element_by_xpath(f"//div[{contadorEmpresa}][contains(@class, 'col-6 col-md-3 associate-wrap-item')]")
    contadorEmpresa +=1

    html_content = element.get_attribute("outerHTML")
    soup = BeautifulSoup(html_content, "html.parser")

    for conteudoTag in soup.findAll("p", limit=4):
        conteudoTag = conteudoTag.get_text()
        conteudoTag = conteudoTag.replace("\t", "")
        conteudoTag = conteudoTag.replace("\n", "")
        conteudoTag = conteudoTag.replace("\r", "")
        conteudoTag = conteudoTag.replace(",", ".")
        conteudoTag = conteudoTag.strip()
        distribuidorConteudo.append(conteudoTag)

        if len(distribuidorConteudo) == 1:

            recebeEmail = 'Ver e-mail' in distribuidorConteudo[0]
            recebeTel = 'Tel.' in distribuidorConteudo[0]
            recebeSite = 'Ver site' in distribuidorConteudo[0]

            formataEmail = distribuidorConteudo[0]
            formtaTel = distribuidorConteudo[0]
            formataSite = distribuidorConteudo[0]

            if recebeEmail == True:
                formataEmail = formataEmail.replace('Ver e-mail', "")
                formataEmail = formataEmail.strip()
                emailCobaia.append(formataEmail)

            elif recebeTel == True:
                formtaTel = formtaTel.replace('Tel.', "")
                formtaTel = formtaTel.strip()
                telefoneCobaia.append(formtaTel)

            elif recebeSite == True:
                formataSite = formataSite.replace('Ver site', "")
                formataSite = formataSite.strip()
                siteCobaia.append(formataSite)
            else:
                empresaCobaia.append(distribuidorConteudo[0])

            distribuidorConteudo.clear()

    if len(empresaCobaia) == 0:
        empresaCobaia.append("null")
    if len(emailCobaia) == 0:
        emailCobaia.append("null")
    if len(telefoneCobaia) == 0:
        telefoneCobaia.append("null")
    if len(siteCobaia) == 0:
        siteCobaia.append("null")

    empresa.append(empresaCobaia[0])
    email.append(emailCobaia[0])
    telefone.append(telefoneCobaia[0])
    site.append(siteCobaia[0])

    empresaCobaia.clear()
    emailCobaia.clear()
    telefoneCobaia.clear()
    siteCobaia.clear()

driver.quit()

#importe o pandas para converter a lista em uma planilha

import pandas as pd

df = pd.DataFrame(columns=['Empresa'])

df['Empresa']=empresa
df['Email']=email
df['Telefone']=telefone
df['Site']=site

print(df)

#writing to Excel

datatoexcel = pd.ExcelWriter('C:/xampp/htdocs/diretorio/Web-Scraping/Relatorios/Scraping-ABSOLAR.xlsx')

# write DataFrame to excel

df.to_excel(datatoexcel)

# save the excel

datatoexcel.save()

print('DataFrame is written to Excel File successfully.')
