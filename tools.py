import datetime
import os.path

from selenium import webdriver
from bs4 import BeautifulSoup
def download_and_parse(url):
    driver = webdriver.Chrome()

    path_to_this = os.path.dirname(__file__)
    #print(path_to_this)

    dir = os.path.join(path_to_this, 'data')
    #print(dir)

    driver.get(url)
    driver.implicitly_wait(2)

    full_title = driver.title
    print("Titel :", full_title)

    title = full_title.split(" - ")
    filename_result = "{}.txt".format(title[0])
    filename_snippet = "{}{}.html".format(load_counter(), title[0])
    write_counter()

    filename_result = os.path.join(dir, filename_result)
    filename_snippet = os.path.join(dir, 'raw_data', filename_snippet)

    source = driver.page_source

    soup = BeautifulSoup(source, features="lxml")

    stew = soup.find(class_="hD5J5m").prettify()

    with open(filename_snippet, 'a', encoding='utf-8') as r:
        r.write(stew)

    r.close()

    dinner = BeautifulSoup(stew, features="lxml").find('span').get_text()
    with open(filename_result, 'a', encoding='utf-8') as r:
        result = dinner.split()
        r.write(result[0] + result[1] + "\n")
        print('Price : ' + result[0] + result[1])

    print()
    r.close()
    driver.close()

def load_counter():
    with open('counter.txt', 'r') as f:
        res = f.read()
    return res

def write_counter():
    temp = load_counter()
    #print(temp)
    temp = int(temp) + 1
    #print(temp)

    with open('counter.txt', 'w') as f:
        f.write('{}'.format(temp))

def parse_pricehtml(file):
    print('Hi')
    with open("Tiger of Sweden EEDIT.html") as html:
        soup = BeautifulSoup(html, features="lxml")

    erg = soup.find(class_="hD5J5m")

    with open("result.html", "w") as r:
        r.write(erg.prettify())

    html = open("result.html")

    res = BeautifulSoup(html).find('span').get_text()

    with open("resultfinal.txt", 'w', encoding='utf-8') as r:
        r.write(res)
    print(res)

def download_pricehtml(url):
    driver = webdriver.Chrome(options="--headless=new")

    driver = webdriver.Chrome()

    driver.get(url)
    driver.implicitly_wait(2)

    fulltitle = driver.title
    print("Titel :", fulltitle)

    title = fulltitle.split(" - ")
    filename = "{}.html".format(title[0])

    with open(filename, "w", encoding='utf-8') as f:
        f.write(driver.page_source)

    f.close()
    driver.close()
