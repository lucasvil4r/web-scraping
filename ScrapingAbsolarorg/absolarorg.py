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

for conteudoTag in soup.find_all("p", limit=4):
    conteudoTag = conteudoTag.get_text()
    conteudoTag = conteudoTag.strip()
    conteudoTag = conteudoTag.replace("\t", " ")
    conteudoTag = conteudoTag.replace("\n", " ")
    distribuidorConteudo.append(conteudoTag)
    if len(distribuidorConteudo) == 4:
        empresa.append(distribuidorConteudo[0])
        email.append(distribuidorConteudo[1])
        telefone.append(distribuidorConteudo[2])
        site.append(distribuidorConteudo[3])

        distribuidorConteudo.clear()

with open('C:/xampp/htdocs/diretorio/Web-Scraping/Relatorios/Scraping-ABSOLAR.csv', 'a', encoding='utf=8') as file:
    tamanhoLista = len(empresa)
    tamanhoLista - 1
    indice = 0
    while indice != tamanhoLista:
        escreveEmpresa = empresa[indice]
        escreveEmail = email[indice]
        escreveTelefone = telefone[indice]
        escreveSite = site[indice]

        escreveEmail = escreveEmail.replace("Ver e-mail", "")
        escreveEmail = escreveEmail.strip()

        escreveSite = escreveSite.replace("Ver site", "")
        escreveSite = escreveSite.strip()

        file.write(f'{escreveEmpresa} § {escreveEmail} § {escreveTelefone} § {escreveSite}')
        file.write('\n')
        indice +=1

    file.close()

driver.quit()
