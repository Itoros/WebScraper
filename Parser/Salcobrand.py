import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)


def extraer(url):

    driver.get(url)
    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    return soup

def Salcobrand(activo):
    url = f'https://salcobrand.cl/search_result?query={activo}'
    soup = extraer(url)
    lista = soup.find_all('div', class_='product clickable')

    for job in lista:
        try:

            descripcionElement = job.find("span", class_="product-info truncate").get_text()
            precio = job.find("span", class_="price selling").get_text()
            link = job.find("a")["href"]

            job = "DESCRIPCION: {}\nPRECIO: {}\nLink: https://salcobrand.cl/{}\n"

            job = job.format(descripcionElement, precio, link)

            print(job)
        except Exception as e:
            print("Exception: {}".format(e))
            pass
