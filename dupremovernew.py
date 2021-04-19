file1 = input('처리할 첫번째 언어 파일명을 확장명과 함께 입력해 주세요 ')
file2 = input('처리할 두번째 언어 파일명을 확장명과 함께 입력해 주세요 ')

save1 = open(input('첫번째 언어쌍 파일을 저장할 파일명을 지정해 주세요(확장명까지 입력해 주세요) '),'w', encoding='UTF8')
save2 = open(input('두번째 언어쌍 파일을 저장할 파일명을 지정해 주세요(확장명까지 입력해 주세요) '),'w', encoding='UTF8')

landict = {}
key = []
val = []

key += [line1.replace('\n', '') for line1 in open(file1, 'r', encoding='UTF8')]
val += [line2.replace('\n', '') for line2 in open(file2, 'r', encoding='UTF8')]
for i in range(len(key)):
    landict[key[i]] = val[i]

key = list(landict.keys())
val = list(landict.values())
landict2 = {}
for i in range(len(key)):
    landict2[val[i]] = key[i]
    
file1final = list(landict2.keys())
file2final = list(landict2.values())

save1.write(str('\n'.join(file2final)))
save1.close()        

save2.write(str('\n'.join(file1final)))
save2.close()  
