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

html_content = element.get_attribute("outerHTML")
soup = BeautifulSoup(html_content, "html.parser")

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
