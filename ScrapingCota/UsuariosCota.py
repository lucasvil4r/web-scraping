import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import  Options

distribuidor = []
status = []
empresa = []
vendedor = []
email = []

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

QtdUsuarioPage = 3
ultimaPage = 1
usuario = 10724
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

        for prod in soup.findAll("td"):
            prod = prod.get_text()
            prod = prod.strip()
            prod = prod.replace("\r", "")
            prod = prod.replace("\t", "")
            prod = prod.replace("\n", "")
            prod = prod.replace(",", "")
            distribuidor.append(prod)
            if len(distribuidor) == 4:
                RemoveStatus = distribuidor[0]
                status.append(distribuidor[0])

                RemoveEmpresa = distribuidor[1]
                empresa.append(distribuidor[1])

                RemoveVendedor = distribuidor[2]
                vendedor.append(distribuidor[2])

                RemoveEmail = distribuidor[3]
                email.append(distribuidor[3])

                distribuidor.remove(RemoveStatus)
                distribuidor.remove(RemoveEmpresa)
                distribuidor.remove(RemoveVendedor)
                distribuidor.remove(RemoveEmail)

with open('C:/xampp/htdocs/diretorio/Web-Scraping/Relatorios.csv/Scraping-COTA.txt', 'a', encoding='utf=8') as file:
    indice = 0
    tamanhoLista = len(empresa)
    while indice != tamanhoLista:
        escreveStatus = status[indice]
        escreveEmpresa = empresa[indice]
        escreveVendedor = vendedor[indice]
        escreveEmail = email[indice]

        escreveStatus = escreveStatus.replace("\r", "")
        escreveStatus = escreveStatus.replace("\t", "")
        escreveStatus = escreveStatus.replace("\n", "")

        escreveEmpresa = escreveEmpresa.replace("\r", "")
        escreveEmpresa = escreveEmpresa.replace("\t", "")
        escreveEmpresa = escreveEmpresa.replace("\n", "")

        escreveVendedor = escreveVendedor.replace("\r", "")
        escreveVendedor = escreveVendedor.replace("\t", "")
        escreveVendedor = escreveVendedor.replace("\n", "")

        escreveEmail = escreveEmail.replace("\r", "")
        escreveEmail = escreveEmail.replace("\t", "")
        escreveEmail = escreveEmail.replace("\n", "")

        file.write(f'{escreveStatus} § {escreveEmpresa} § {escreveVendedor} § {escreveEmail}')
        file.write('\n')
        indice +=1

    file.close()

driver.quit()
