def selection():
    while True:
        global sublan
        sublan = input("다운받을 Ted talk의 자막 언어를 언어 코드로 입력해주세요(가능 언어:ar, de, en, fr, it, ja, ko, mn, pt, ru, sv, vi, zhs, zht) ")
        if sublan == 'ar':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[5]/a'
            language = '//button[@data-title="[TXT] العربية"]'
            break
        elif sublan == 'de':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[38]/a'
            language = '//button[@data-title="[TXT] Deutsch"]'
            break
        elif sublan == 'en':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[28]/a'
            language = '//button[@data-title="[TXT] English"]'
            break
        elif sublan == 'fr':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[34]/a'
            language = '//button[@data-title="[TXT] Français"]'
            break
        elif sublan == 'it':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[52]/a'
            language = '//button[@data-title="[TXT] Italiano"]'
            break
        elif sublan == 'ja':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[53]/a'
            language = '//button[@data-title="[TXT] 日本語"]'
            break
        elif sublan == 'ko':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[58]/a'
            language = '//button[@data-title="[TXT] 한국어"]'
            break
        elif sublan == 'mn':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[75]/a'
            language = '//button[@data-title="[TXT] Монгол"]'
            break
        elif sublan == 'pt':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[84]/a'
            language = '//button[@data-title="[TXT] Português de Portugal"]'  
            break
        elif sublan == 'ru':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[88]/a'
            language = '//button[@data-title="[TXT] Русский"]'  
            break
        elif sublan == 'sv':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[100]/a'
            language = '//button[@data-title="[TXT] Svenska"]'  
            break    
        elif sublan == 'vi':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[115]/a'
            language = '//button[@data-title="[TXT] Tiếng Việt"]'  
            break  
        elif sublan == 'zhs':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[19]/a'
            language = '//button[@data-title="[TXT] 中文 (简体)"]'  
            break    
        elif sublan == 'zht':
            subtitle = '/html/body/div[3]/div[2]/div/div/div/div[3]/ul/li[20]/a'
            language = '//button[@data-title="[TXT] 中文 (繁體)"]'  
            break        
        else:
            print('정확한 언어 코드를 입력해 주세요.')
    return sublan, subtitle, language
        