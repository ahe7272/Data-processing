import webbrowser
from selenium import webdriver
import time

def openpage():
    while True:
        global sublan
        sublan = input("Ted talk의 자막 언어를 언어 코드로 입력해주세요(가능 언어:ar, de, en, fr, it, ja, ko, mn, pt, ru, sv, vi, zhs, zht) ")
        if sublan == 'ar':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[5]/a'
            break
        elif sublan == 'de':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[38]/a'
            break
        elif sublan == 'en':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[28]/a'
            break
        elif sublan == 'fr':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[34]/a'
            break
        elif sublan == 'it':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[52]/a'
            break
        elif sublan == 'ja':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[53]/a'
            break
        elif sublan == 'ko':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[58]/a'
            break
        elif sublan == 'mn':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[75]/a'
            break
        elif sublan == 'pt':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[84]/a'
            break
        elif sublan == 'ru':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[88]/a'
            break
        elif sublan == 'sv':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[100]/a'
            break    
        elif sublan == 'vi':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[115]/a'
            break  
        elif sublan == 'zhs':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[19]/a'
            break    
        elif sublan == 'zht':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[20]/a'
            break        
        else:
            print('정확한 언어 코드를 입력해 주세요.')
        
    #Ted talk page 열고 찾는 언어쌍으로 비디오 검색
    driver = webdriver.Chrome(r'/mnt/c/Users/ccc/Desktop/DATA/DATA_EXTRACT/TED Parsing/chromedriver.exe')
    driver.maximize_window()
    driver.get('https://www.ted.com/talks')
    driver.find_element_by_xpath('//*[@id="languages"]').click()
    driver.find_element_by_xpath('//*[@id="languages"]/option[3]').click()
    time.sleep(2)
    driver.find_element_by_xpath(subtitle).click()
    return driver

