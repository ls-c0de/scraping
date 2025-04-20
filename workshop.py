from selenium import webdriver
from bs4 import BeautifulSoup
def feeder(base_url, filter):
    driver = webdriver.Chrome()
    driver.get(base_url)

    soup = BeautifulSoup(driver.page_source, features="lxml")

    urllist = []

    counter = 1
    for a in soup.find_all('a', href=True):
        if a['href'].startswith(filter):
            urllist.append(a['href'])
            #print(counter, " Found URL: ", a['href']) #debugging purpose

        if a['href'].startswith("#"):
            break
        counter += 1

    return urllist

