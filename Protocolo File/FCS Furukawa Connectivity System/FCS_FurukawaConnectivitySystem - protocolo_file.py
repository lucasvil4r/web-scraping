import urllib.request
from bs4 import BeautifulSoup

pag = 0

while pag != 100:
    pag +=1
    url = (f'file:///C:/xampp/htdocs/diretorio/Web-Scraping/FCS%20Furukawa%20Connectivity%20System/Page={pag}/Broadband%20e%20Cabling%20System,%20confiabilidade%20dos%20materiais%20empregados%20_%20Furukawa%20Electric%20LatAm.html')
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    descricao = soup.find_all('p', attrs={'product-name title break-all'})
    especificao = soup.find_all('p', attrs={'pb-3 fillterBy'})

    for prod in descricao:
        descri = prod.get_text()
        print(descri)    
