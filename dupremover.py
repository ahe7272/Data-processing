file_1 = input('처리할 첫번째 언어 파일명을 확장명과 함께 입력해 주세요 ')
file_2 = input('처리할 두번째 언어 파일명을 확장명과 함께 입력해 주세요 ')

distinctlines1 = []
count1 = 0
dup_index = []
lines1 = []
lines2 = []
 #같은 문장이 있으면 모두 삭제

with open(file_1, 'r', encoding='UTF8') as f1:  
    global total1  
    total1 = f1.read().count('\n')+1

with open(file_1, 'r', encoding='UTF8') as f1:    
    for i in f1.read().split('\n'):
        lines1.append(i)
        if i not in distinctlines1:
            distinctlines1.append(i)
        elif i in distinctlines1:
            dup_index.append(count1)
            dup_index.append(lines1.index(i))   
        count1 += 1
        if count1 == round(total1*0.01):
            print('중복 줄을 찾고 있습니다...')            
        elif count1 == round(total1*0.1):
            print('파일의 1/10를 확인했습니다.') 
        elif count1 == round(total1*0.2):
            print('파일의 2/10를 확인했습니다.')
        elif count1 == round(total1*0.3):
            print('파일의 3/10를 확인했습니다.')
        elif count1 == round(total1*0.4):
            print('파일의 4/10를 확인했습니다.')            
        elif count1 == round(total1*0.5):
            print('파일의 5/10를 확인했습니다.')  
        elif count1 == round(total1*0.6):
            print('파일의 6/10를 확인했습니다.')
        elif count1 == round(total1*0.7):
            print('파일의 7/10를 확인했습니다.')
        elif count1 == round(total1*0.8):
            print('파일의 8/10를 확인했습니다.')     
        elif count1 == round(total1*0.9):
            print('파일의 9/10를 확인했습니다.')
        elif count1 == total1:
            print('첫번째 파일을 모두 확인 했습니다.')

distinctlines2 = []
count2 = 0
print()

with open(file_2, 'r', encoding='UTF8') as f2:  
    global total2
    total2 = f2.read().count('\n')+1

with open(file_2, 'r', encoding='UTF8') as f2:
    for i in f2.read().split('\n'):
        lines2.append(i)
        if i not in distinctlines2:
            distinctlines2.append(i)
        elif i in distinctlines2 and count2 not in dup_index:
            dup_index.append(count2)    
            dup_index.append(lines2.index(i))   
        count2 += 1      
        if count2 == round(total2*0.01):
            print('중복 줄을 찾고 있습니다...')            
        elif count2 == round(total2*0.1):
            print('파일의 1/10를 확인했습니다.') 
        elif count2 == round(total2*0.2):
            print('파일의 2/10를 확인했습니다.')
        elif count2 == round(total2*0.3):
            print('파일의 3/10를 확인했습니다.')
        elif count2 == round(total2*0.4):
            print('파일의 4/10를 확인했습니다.')            
        elif count2 == round(total2*0.5):
            print('파일의 5/10를 확인했습니다.')  
        elif count2 == round(total2*0.6):
            print('파일의 6/10를 확인했습니다.')
        elif count2 == round(total2*0.7):
            print('파일의 7/10를 확인했습니다.')
        elif count2 == round(total2*0.8):
            print('파일의 8/10를 확인했습니다.')     
        elif count2 == round(total2*0.9):
            print('파일의 9/10를 확인했습니다.')
        elif count2 == total2:
            print('두번째 파일을 모두 확인 했습니다.')

for i in list(sorted(set(dup_index)))[::-1]:
    del lines1[i]
    del lines2[i]

fname1 = open(input('첫번째 언어쌍 파일을 저장할 파일명을 지정해 주세요(확장명까지 입력해 주세요) '),'w', encoding='UTF8')
fname2 = open(input('두번째 언어쌍 파일을 저장할 파일명을 지정해 주세요(확장명까지 입력해 주세요) '),'w', encoding='UTF8')

fname1.write(str('\n'.join(lines1)))
fname1.close()        

fname2.write(str('\n'.join(lines2)))
fname2.close()  
