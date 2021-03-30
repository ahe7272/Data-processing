file_1 = input('병합할 첫번째 파일명을 확장명과 함께 입력해 주세요 ')
file_2 = input('병합할 두번째 파일명을 확장명과 함께 입력해 주세요 ')

distinctlines1 = []
count1 = 0
dup_index = []
lines1 = []
lines2 = []

#같은 문장이 있으면 모두 삭제
with open(file_1, 'r') as f1:    
    for i in f1.read().split('\n'):
        lines1.append(i)
        if i not in distinctlines1:
            distinctlines1.append(i)
        elif i in distinctlines1:
            dup_index.append(count1)
            dup_index.append(lines1.index(i))   
        count1 += 1

distinctlines2 = []
count2 = 0

with open(file_2, 'r') as f2:
    for i in f2.read().split('\n'):
        lines2.append(i)
        if i not in distinctlines2:
            distinctlines2.append(i)
        elif i in distinctlines2 and count2 not in dup_index:
            dup_index.append(count2)    
            dup_index.append(lines2.index(i))   
        count2 += 1      

print(set(dup_index).reverse())
"""
for i in set(dup_index.sort(reverse=True)):
    print(lines1[i])
    print(lines2[i])


distinctfile1 = []
distinctfile2 = []
for line in joined:
    distinctfile1.append(line.split('\t')[-1])
    distinctfile2.append(line.split('\t')[0])

fname1 = open(input('첫번째 언어쌍 파일을 저장할 파일명을 지정해 주세요(확장명까지 입력해 주세요) '),'w')
fname2 = open(input('두번째 언어쌍 파일을 저장할 파일명을 지정해 주세요(확장명까지 입력해 주세요) '),'w')

fname1.write(str('\n'.join(distinctfile1)))
fname1.close()        

fname2.write(str('\n'.join(distinctfile2)))
fname2.close()  
"""