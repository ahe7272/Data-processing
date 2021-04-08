import requests
from bs4 import BeautifulSoup
import webbrowser
from selenium import webdriver
import time
import sublangauge
import re

def links():
    driver = sublangauge.openpage()
    url = driver.current_url
    driver.close()
    response = requests.get(url)
    link_list = []
    full_links = []
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a', class_="ga-link"):
            if re.search("^/talks/",link.get('href')): 
                link_list.append(link.get('href'))
    else : 
        print(response.status_code)
    for i in link_list[::2]:
        full_url = 'https://www.ted.com' +re.sub("\?language.*$", "", i)
        full_links.append(full_url)
    return full_links

