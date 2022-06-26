import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from DataManager import save_file

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)


def extraer(url):

    driver.get(url)
    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    return soup

def Salcobrand(remedios,lista2):

    for i in remedios:

        url = f'https://salcobrand.cl/search_result?query={i}'
        soup = extraer(url)
        lista = soup.find_all('div', class_='product clickable')

        for job in lista:
            try:
                print(f"Principio activo:{i}")
                descripcionElement = job.find("span", class_="product-info truncate").get_text()
                precio = job.find("span", class_="price selling").get_text()

                lista2.append(descripcionElement)
                lista2.append("Salcobrand")
                lista2.append(precio[18:])
                lista2.append("\n")


            except Exception as e:
                print("Exception: {}".format(e))
                pass

    return lista2

