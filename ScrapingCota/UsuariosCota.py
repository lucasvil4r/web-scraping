import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import  Options

distribuidorConteudo = []
status = []
empresa = []
vendedor = []
email = []
cadastro = []

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\xampp\htdocs\diretorio\Web-Scraping\ScrapingCota\chromedriver.exe')
#driver = webdriver.Chrome(executable_path=r'C:\xampp\htdocs\diretorio\Web-Scraping\ScrapingCota\chromedriver.exe')

url = (f'https://gpcabling.com.br/session')
driver.get(url)

time.sleep(2)

email_element = driver.find_element_by_id('email')
passowrd_element = driver.find_element_by_id('password')

email_element.send_keys('lucas@gpcabling.com.br')
passowrd_element.send_keys('sofia789@')

driver.find_element_by_xpath("//button[@class='btn btn-primary btn-large']").click()

QtdUsuarioPage = 125
ultimaPage = 1
usuario = 10737
page = 0
while page != ultimaPage:
    cont = 0
    page +=1
    driver.get(f'https://gpcabling.com.br/usuario/index?page={page}')

    time.sleep(2)

    while cont != QtdUsuarioPage:
        cont +=1
        element = driver.find_element_by_id('tb-user-status')
        element = driver.find_element_by_id(f'row-user-{usuario}')
        usuario = usuario - 1

        html_content = element.get_attribute("outerHTML")
        soup = BeautifulSoup(html_content, 'html.parser')

        for conteudoTag in soup.find_all("td", limit=5):
            conteudoTag = conteudoTag.get_text()
            conteudoTag = conteudoTag.strip()
            conteudoTag = conteudoTag.replace("\r", "")
            conteudoTag = conteudoTag.replace("\t", "")
            conteudoTag = conteudoTag.replace("\n", "")
            conteudoTag = conteudoTag.replace(",", "")
            distribuidorConteudo.append(conteudoTag)
            if len(distribuidorConteudo) == 5:
                status.append(distribuidorConteudo[0])
                empresa.append(distribuidorConteudo[1])
                vendedor.append(distribuidorConteudo[2])
                email.append(distribuidorConteudo[3])
                cadastro.append(distribuidorConteudo[4])

                distribuidorConteudo.clear()

with open('C:/xampp/htdocs/diretorio/Web-Scraping/Relatorios/Scraping-COTA.csv', 'a', encoding='utf=8') as file:
    indice = 0
    tamanhoLista = len(empresa)
    tamanhoLista - 1
    while indice != tamanhoLista:
        escreveStatus = status[indice]
        escreveEmpresa = empresa[indice]
        escreveVendedor = vendedor[indice]
        escreveEmail = email[indice]
        escreveCadastro = cadastro[indice]

        file.write(f'{escreveStatus} § {escreveEmpresa} § {escreveVendedor} § {escreveEmail} § {escreveCadastro}')
        file.write('\n')
        indice +=1

    file.close()

driver.quit()
