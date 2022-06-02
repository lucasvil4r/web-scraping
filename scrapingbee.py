'''
import urllib3

user_agent_header = urllib3.make_headers(user_agent="<USER AGENT>")
pool = urllib3.ProxyManager(f'<PROXY IP>', headers=user_agent_header)
r = pool.request('GET', 'https://www.furukawalatam.com/pt-br/catalogo-de-produtos-categoria/FCS/')
print(r.data)
'''

import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.furukawalatam.com/pt-br/catalogo-de-produtos-categoria/FCS/')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.findAll('p', class_='product-name title break-all')

print(links)