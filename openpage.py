import webbrowser
from selenium import webdriver
import time
import lanselect

sublan, subtitle, language = lanselect.selection()

def open_page():
    #Ted talk page 열고 찾는 언어쌍으로 비디오 검색
    driver = webdriver.Chrome(r'/mnt/c/Users/ccc/Desktop/DATA/DATA_EXTRACT/TED Parsing/chromedriver.exe')
    driver.maximize_window()
    driver.get('https://www.ted.com/talks')
    driver.find_element_by_xpath('//*[@id="languages"]').click()
    driver.find_element_by_xpath('//*[@id="languages"]/option[3]').click()
    time.sleep(2)
    driver.find_element_by_xpath(subtitle).click()
    return driver
