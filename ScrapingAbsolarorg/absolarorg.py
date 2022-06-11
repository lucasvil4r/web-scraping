import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import  Options

distribuidorConteudo = []
empresa = []
email = []
telefone = []
site = []

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\xampp\htdocs\diretorio\Web-Scraping\ScrapingAbsolarorg\chromedriver.exe')
#driver = webdriver.Chrome(executable_path=r'C:\xampp\htdocs\diretorio\Web-Scraping\ScrapingAbsolarorg\chromedriver.exe')

url = (f'https://www.absolar.org.br/nossos-associados/')
driver.get(url)

time.sleep(10)

element = driver.find_element_by_xpath("//div[@class='row associates-itens']")

qtdEmpresaPage = 11
cont = 1

while cont != qtdEmpresaPage:
    element = driver.find_element_by_xpath(f"//div[{cont}][contains(@class, 'col-6 col-md-3 associate-wrap-item')]")
    cont +=1

    html_content = element.get_attribute("outerHTML")
    soup = BeautifulSoup(html_content, "html.parser")

    for conteudoTag in soup.findAll("p", limit = 4):
        conteudoTag = conteudoTag.get_text()
        conteudoTag = conteudoTag.replace("\t", " ")
        conteudoTag = conteudoTag.replace("\n", " ")
        conteudoTag = conteudoTag.replace("\r", "")
        conteudoTag = conteudoTag.replace(",", ".")
        conteudoTag = conteudoTag.strip()
        distribuidorConteudo.append(conteudoTag)
        qtdDistribuidor = len(distribuidorConteudo)

        if len(distribuidorConteudo) == 4:
            empresa.append(distribuidorConteudo[0])

            recebeEmail = 'Ver e-mail' in distribuidorConteudo[1]
            if recebeEmail == True:
                email.append(distribuidorConteudo[1])
            elif recebeEmail == False:
                email.insert(1, "Null")

            recebeTel = 'Tel' in distribuidorConteudo[2]
            if recebeTel == True:
                telefone.append(distribuidorConteudo[2])
            elif recebeTel == False:
                telefone.insert(2, "Null")

            recebeSite = 'Ver site' in distribuidorConteudo[3]
            if recebeSite == True:
                site.append(distribuidorConteudo[3])
            elif recebeSite == False:
                site.insert(3, "Null")

            distribuidorConteudo.clear()

driver.quit()

#importe o pandas para converter a lista em uma planilha

import pandas as pd

df = pd.DataFrame(columns=['Empresa'])

df['Empresa']=empresa
df['Email']=email
df['Telefone']=telefone
df['Site']=site

print(df)

'''
#writing to Excel

datatoexcel = pd.ExcelWriter('C:/xampp/htdocs/diretorio/Web-Scraping/Relatorios/Scraping-ABSOLAR.xlsx')

# write DataFrame to excel

df.to_excel(datatoexcel)

# save the excel

datatoexcel.save()

print('DataFrame is written to Excel File successfully.')
'''