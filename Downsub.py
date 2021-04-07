import webbrowser
from selenium import webdriver
import time
import linkmaker

url_list= linkmaker.links()

driver = webdriver.Chrome(r'/mnt/c/Users/ccc/Desktop/DATA/DATA_EXTRACT/TED Parsing/chromedriver.exe')
driver.maximize_window()

def subtitle_finder():
  for url in url_list:
    driver.get('https://downsub.com')
    element = driver.find_element_by_name('url')
    element.send_keys(url)
    time.sleep(3)
    try: 
      English = driver.find_element_by_xpath('//button[@data-title="[TXT] English"]').click()
      time.sleep(0.5)
    except:
      print('No subtitle file.')
    driver.close()

subtitle_finder()

