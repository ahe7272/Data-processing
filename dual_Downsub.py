import webbrowser
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import linkmaker
import openpage
import lanselect

url_list= linkmaker.links()
print()
print('쌍으로 다운 받을 자막 언어를 선택합니다.')
print()
chosenlan1, subtitle, language1= lanselect.selection()
chosenlan2, subtitle, language2= lanselect.selection()
driver = webdriver.Chrome(r'/mnt/c/Users/ccc/Desktop/DATA/DATA_EXTRACT/TED Parsing/chromedriver.exe')
driver.maximize_window()

def subtitle_finder():
  driver.get('https://downsub.com')
  for url in url_list:
    element = driver.find_element_by_name('url')
    element.send_keys(url, Keys.ENTER)
    time.sleep(1)  
    try: 
      if driver.find_element_by_xpath(language1) and driver.find_element_by_xpath(language2):
        driver.find_element_by_xpath(language1).click()
        driver.find_element_by_xpath(language2).click()  
        time.sleep(1)
    except:
      print()
      print("비디오 링크: \n" + url + '\n비디오에 선택한 자막이 없습니다.' )
      print()
    driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[1]/div/div[2]/form/div/div[1]/div[1]/div[2]/div/button').click()
  driver.close()
  return 

subtitle_finder()


