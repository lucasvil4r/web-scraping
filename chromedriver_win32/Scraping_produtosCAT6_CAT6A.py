from selenium import webdriver
from selenium.webdriver.chrome.options import Options



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=r'C:\xampp\htdocs\diretorio\Web-Scraping\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)
driver.get('file:///C:/Users/lucas.GPCABLING/Downloads/Broadband%20e%20Cabling%20System,%20confiabilidade%20dos%20materiais%20empregados%20_%20Furukawa%20Electric%20LatAm.html')
print(driver.page_source)
driver.quit()
