import requests
from bs4 import BeautifulSoup

def has_data_search(tag):
    return tag.has_attr("data-container")


def Ahumada(principio_activo):

    url = f"https://www.farmaciasahumada.cl/catalogsearch/result/index/?p=1&q={principio_activo}"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    print(soup)
    results = soup.find_all(has_data_search)

    while(True):

        for job in results:
            try:
                titleElement = job.find("p", class_="product-brand-name").get_text()
                descripcionElement = job.find("a", class_="product-item-link").get_text()
                precio = job.find("span", class_="price").get_text()
                link = job.find("a", class_="product-item-link")["href"]

                job = "NOMBRE: {}\nDESCRIPCION: {}\nPRECIO: {}\nLink: {}\n"

                job = job.format(titleElement, descripcionElement, precio, link)

                print(job)
            except Exception as e:
                print("Exception: {}".format(e))
                pass

        try:
            sgt = soup.find("a", class_="action next")["href"]
            url = sgt
        except:
            break
    return