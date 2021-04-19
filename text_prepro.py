import re

filename = input('정제할 파일명을 확장명과 함께 입력해 주세요(예:ko.txt) ')

def prepro():
    with open(filename, 'r', encoding='UTF-8') as f:   
        text = ""
        for i in f.readlines():                
            #필수기호 띄어쓰기 제거 및 정제 regex
            i = re.sub("^[\.,+\-_\)\]\}\|\~\!\?:;\*\–\－]+", '', i)
            i = re.sub("[,+\-_\(\[\{\|\~:;\*\–\－]+$", "", i)
            i = re.sub(";+", "", i)
            i = re.sub("\s+\.", ".", i)
            i = re.sub("\s+,", ",", i)
            i = re.sub("\s+\?+", "?", i)
            i = re.sub("\s+\!+", "!", i)
            i = re.sub("\--+", "", i)
            i = re.sub("＄", "$", i)
            i = re.sub('^[0-9]+$', '', i)
            #re.sub(r'\[.*\]', '', i)
            #re.sub(r'\(.*\)', '', i)

            #HTML 기호변경 regex  
            i = re.sub("&lt;", '<', i)
            i = re.sub("&gt;", '>', i)
            i = re.sub("&#34;", '"', i)
            i = re.sub("&quot;", '"', i)
            i = re.sub("&#38;", '&', i)
            i = re.sub("&amp;", '&', i)
            i = re.sub("&#160;", '', i)
            i = re.sub("&nbsp;", '', i)
            i = re.sub("&#176;", '.', i)
            i = re.sub("&deg;", '.', i)

            #특수기호 삭제 regex
            i = re.sub('(?!\r|\n)[\x00-\x1f\x80-\x9f]', '', i)
            i = re.sub("[•●■▲�♫↔→「」【】『』±￢ªⓒ《》º\¸·¶´¨…－]", "", i)
            i = re.sub("\s\*", '', i)          
            i = re.sub('➋', '2', i)
            i = re.sub('➌', '3', i)
            i = re.sub('➍', '4', i)
            i = re.sub('➎', '5', i)
            i = re.sub('➏', '6', i)
            i = re.sub("&#167;", '', i) 				
            i = re.sub("&sect;", '', i)
            i = re.sub("&#168;", '', i)
            i = re.sub("&uml;", '', i)
            i = re.sub("&#169;", '', i)
            i = re.sub("&copy;", '', i)
            i = re.sub("&#170;", '', i)
            i = re.sub("&ordf;", '', i)
            i = re.sub("&#172;", '', i)
            i = re.sub("&not;", '', i)
            i = re.sub("&#177;", '', i)
            i = re.sub("&plusmn;", '', i)
            i = re.sub("&#178;", '', i)
            i = re.sub("&sup2;", '', i)
            i = re.sub("¹", '1', i)
            i = re.sub("²", '2', i)
            i = re.sub("³", '3', i)
            i = re.sub("&#179;", '', i)
            i = re.sub("&sup3;", '', i)
            i = re.sub("&#180;", '', i)
            i = re.sub("&acute;", '', i)
            #re.sub("&#181;", 'μ', i)    #for Greek  
            #re.sub("&micro;", 'μ', i)
            i = re.sub("&#181;", '', i)
            i = re.sub("&micro;", '', i)
            i = re.sub("&#182;", '', i)
            i = re.sub("&para;", '', i)
            i = re.sub("&#183;", '', i)
            i = re.sub("&middot;", '', i)
            i = re.sub("&cedil;", '', i)
            i = re.sub("&#184;", '', i)
            i = re.sub("&sup1;", '', i)
            i = re.sub("&#185;", '', i)
            i = re.sub("&#186;", '', i)
            i = re.sub("&ordm;", '', i)
            i = re.sub("½", '1/2', i)
            i = re.sub("¼", '1/4', i)
            i = re.sub("&#188;", '', i)
            i = re.sub("&frac14;", '', i)
            i = re.sub("¾", '3/4', i)
            i = re.sub("&#189;", '', i)
            i = re.sub("&frac12;", '', i)     
            i = re.sub("&#190;", '', i)
            i = re.sub("&frac34;", '', i)
            i = re.sub("&#187;", '', i)   
            i = re.sub("&raquo;", '', i)
            i = re.sub("≫", '"', i)
            i = re.sub("&#171;", '', i)   
            i = re.sub("&laquo;", '', i)
            i = re.sub("≪", '"', i)	

            if language == 'es':
                i = re.sub("&#191;", '¿', i)     
                i = re.sub("&iquest;", '¿', i)
                i = re.sub("&iexcl;", '¡', i)
            else:
                i = re.sub("&#191;", '', i)     
                i = re.sub("&iquest;", '', i)
                i = re.sub("&iexcl;", '', i)
                i = re.sub("¡", '', i)
                i = re.sub("¿", '', i)	
            if language == 'zh':
                i = re.sub('\.', '。', i)
                i = re.sub(',', '、', i)
                i = re.sub(',', '，', i)
                i = re.sub(')', '）', i)
                i = re.sub('(', '（', i)
                i = re.sub(':', '：', i)
            else:
                i = re.sub('。', '.', i)
                i = re.sub('、', ',', i)
                i = re.sub('，', ',', i)
                i = re.sub('）', ')', i)
                i = re.sub('（', '(', i)
                i = re.sub('：', ':', i)
            text += i
    f.close()
    return text
    
"""   
#각 라인당 혼자 있는 ' " ` 기호 제거

if i.count("‘") == 1:
    i = re.sub("^[‘]", "", i)
    i = re.sub("[‘]$", "", i)
if i.count("’") == 1:
    i = re.sub("^[’]", "", i)
    i = re.sub("[’]$", "", i)
if i.count("“") == 1:
    i = re.sub("^[“]", "", i)
    i = re.sub("[“]$", "", i)
"""
    

while True: 
    global language
    language = input('정제할 언어 코드를 선택해 주세요(스페인어: es, 중국어:zh, 그외:else) ')
    if language in ('es', 'zh', 'else'):
        global result
        result = prepro()      
        break
    else:
        print('옵션에 맞게 다시 답해주세요.')

file = open(input('결과를 저장할 파일명을 확장명과 함께 입력해 주세요 '), 'w')
file.write(result)
file.close()
