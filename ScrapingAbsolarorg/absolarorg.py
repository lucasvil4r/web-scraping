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

time.sleep(5)

element = driver.find_element_by_xpath("//div[@class='row associates-itens']")

element = driver.find_element_by_xpath(f"//div[{12}][contains(@class, 'col-6 col-md-3 associate-wrap-item')]")

html_content = element.get_attribute("outerHTML")
soup = BeautifulSoup(html_content, "html.parser")

for conteudoTag in soup.findAll("p", limit=4):
    conteudoTag = conteudoTag.get_text()
    conteudoTag = conteudoTag.replace("\t", " ")
    conteudoTag = conteudoTag.replace("\n", " ")
    conteudoTag = conteudoTag.replace("\r", "")
    conteudoTag = conteudoTag.replace(",", ".")
    conteudoTag = conteudoTag.strip()
    distribuidorConteudo.append(conteudoTag)

    if len(distribuidorConteudo) == 1:


        if '@' in distribuidorConteudo[0]:
            email.append(distribuidorConteudo[0])
            distribuidorConteudo.pop(0)
        else:
            email.append(" ")
        

        elif 'Tel. (' in distribuidorConteudo[0]:
            telefone.append(distribuidorConteudo[0])
            distribuidorConteudo.pop(0)
        else:

            telefone.append(" ")

        elif 'Ver site' in distribuidorConteudo[0]:

            site.append(distribuidorConteudo[0])
            distribuidorConteudo.pop(0)

        else:
            
            site.append(" ")
        
        empresa.append(distribuidorConteudo[0])
        distribuidorConteudo.pop(0)








































'''
for conteudoTag in soup.findAll("p", limit=4):
    conteudoTag = conteudoTag.get_text()
    conteudoTag = conteudoTag.strip()
    conteudoTag = conteudoTag.replace("\t", " ")
    conteudoTag = conteudoTag.replace("\n", " ")
    conteudoTag = conteudoTag.replace("Ver e-mail", "")
    conteudoTag = conteudoTag.replace("Ver site", "")
    conteudoTag = conteudoTag.strip()
    distribuidorConteudo.append(conteudoTag)
    if len(distribuidorConteudo) == 4:
        empresa.append(distribuidorConteudo[0])
        email.append(distribuidorConteudo[1])
        telefone.append(distribuidorConteudo[2])
        site.append(distribuidorConteudo[3])








for test in soup:
    conteudoTagEmpresa = test.find("p", attrs={'my-3 absolar-text-13'})
    conteudoTagEmail = test.find("p", attrs={'tooltip1'})
    conteudoTagSite = test.find("span", attrs={'tooltiptext'})

    conteudoTagEmpresa = conteudoTagEmpresa.get_text()
    conteudoTagEmpresa = conteudoTagEmpresa.strip()
    conteudoTagEmpresa = conteudoTagEmpresa.replace("\t", "")
    conteudoTagEmpresa = conteudoTagEmpresa.replace("\n", "")
    empresa.append(conteudoTagEmpresa)

    conteudoTagEmail = conteudoTagEmail.get_text()
    conteudoTagEmail = conteudoTagEmail.strip()
    conteudoTagEmail = conteudoTagEmail.replace("\t", "")
    conteudoTagEmail = conteudoTagEmail.replace("\n", "")
    email.append(conteudoTagEmail)

    conteudoTagTelefone = conteudoTagTelefone.get_text()
    conteudoTagTelefone = conteudoTagTelefone.strip()
    conteudoTagTelefone = conteudoTagTelefone.replace("Ver site", "")
    conteudoTagTelefone = conteudoTagTelefone.replace("\t", "")
    conteudoTagTelefone = conteudoTagTelefone.replace("\n", "")
    telefone.append(conteudoTagTelefone)

    conteudoTagSite = conteudoTagSite.get_text()
    conteudoTagSite = conteudoTagSite.strip()
    conteudoTagSite = conteudoTagSite.replace("Ver site", "")
    conteudoTagSite = conteudoTagSite.replace("\t", "")
    conteudoTagSite = conteudoTagSite.replace("\n", "")
    site.append(conteudoTagSite)

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
'''

driver.quit()
