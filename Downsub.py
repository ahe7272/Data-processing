#cat source.txt | findstr "href='/talks/" | -replace ("<a class=' ga-link' data-ga-context='talks' href='/","")} | -replace ('>', "")} > Ted_link.txt

import webbrowser
from selenium import webdriver
import time

def link_maker(file):
  with open(file) as f:
    for lines in f.readlines():
      driver = webdriver.Chrome(r'/mnt/c/Users/ccc/Desktop/DATA/DATA_EXTRACT/TED Parsing/chromedriver.exe')
      driver.get('https://downsub.com')
      element = driver.find_element_by_name('url')
      element.send_keys('https://www.ted.com/'+str(lines))
      time.sleep(0.5)
      try: 
        English = driver.find_element_by_xpath('//button[@data-title="[TXT] English"]').click()
        time.sleep(0.5)
      except:
        print('No subtitle file.')
      driver.close()

print(link_maker('JA_link2.txt'))

