import webbrowser
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import linkmaker
import sublangauge

url_list= linkmaker.links()

chosenlan = sublangauge.chosenlan()
if chosenlan ==  'ar': 
  language = '//button[@data-title="[TXT] العربية"]'
elif chosenlan == 'de':
  language = '//button[@data-title="[TXT] Deutsch"]'
elif chosenlan == 'en':
  language = '//button[@data-title="[TXT] English"]'
elif chosenlan == 'fr':
  language = '//button[@data-title="[TXT] Français"]'
elif chosenlan == 'it':
  language = '//button[@data-title="[TXT] Italiano"]'
elif chosenlan == 'ja':
  language = '//button[@data-title="[TXT] 日本語"]'
elif chosenlan == 'ko':
  language = '//button[@data-title="[TXT] 한국어"]'
elif chosenlan == 'mn':
  language = '//button[@data-title="[TXT] Монгол"]'
elif chosenlan == 'pt':
  language = '//button[@data-title="[TXT] Português de Portugal"]'
elif chosenlan == 'ru':
  language = '//button[@data-title="[TXT] Русский"]'
elif chosenlan == 'sv':
  language = '//button[@data-title="[TXT] Svenska"]'
elif chosenlan == 'vi':
  language = '//button[@data-title="[TXT] Tiếng Việt"]'
elif chosenlan == 'zhs':
  language = '//button[@data-title="[TXT] 中文 (简体)"]'
elif chosenlan == 'zht':
  language = '//button[@data-title="[TXT] 中文 (繁體)"]'
   

driver = webdriver.Chrome(r'/mnt/c/Users/ccc/Desktop/DATA/DATA_EXTRACT/TED Parsing/chromedriver.exe')
driver.maximize_window()

def subtitle_finder():
  driver.get('https://downsub.com')
  for url in url_list:
    element = driver.find_element_by_name('url')
    element.send_keys(url, Keys.ENTER)
    time.sleep(1)  
    try: 
      driver.find_element_by_xpath(language).click()
      time.sleep(1)
    except:
      print()
      print("비디오 링크: \n" + url + '\n비디오에 선택한 자막이 없습니다.' )
      print()
    driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[1]/div/div[2]/form/div/div[1]/div[1]/div[2]/div/button').click()
  driver.close()
  return 

subtitle_finder()


