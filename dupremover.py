try:
    file_1 = input('병합할 첫번째 파일명을 확장명과 함께 입력해 주세요')
    file_2 = input('병합할 두번째 파일명을 확장명과 함께 입력해 주세요')
except:
    print('일치하는 파일이 없습니다.')

distinctlines1 = []
count1 = 0
dup_index = []
with open(file_1, 'r') as f1:
    for i in f1.readlines():
        if i not in distinctlines1:
            distinctlines1.append(i)
        if i in distinctlines1:
            dup_index.append(count1)
        count1 += 1

distinctlines2 = []
count2 = 0
with open(file_2, 'r') as f2:
    for i in f2.readlines():
        if i not in distinctlines2:
            distinctlines1.append(i)
        if i in distinctlines2 and count2 not in dup_index:
            dup_index.append(count2)    
        count2 += 1

lines1 = []
lines2 = []
joined = []
with open(file_1, 'r') as f1:
    for i in f1.readlines():
        lines1.append(i)
with open(file_2) as f2:
    for i in f2.readlines():
        lines2.append(i)
for i in range(len(lines1)):
    joined.append((lines1[i]+'\t'+lines2[i]))

for i in dup_index:
    del joined[i]
        
distinctfile1 = []
distinctfile2 = []
for line in joined:
    distinctfile1.append(line.split('\t')[-1])
    distinctfile2.append(line.split('\t')[0])

fname1 = open(input('첫번째 언어쌍 파일을 저장할 파일명을 지정해 주세요(확장명까지 입력해 주세요)'),'w')
fname2 = open(input('두번째 언어쌍 파일을 저장할 파일명을 지정해 주세요(확장명까지 입력해 주세요)'),'w')

fname1.write(str('\n'.join(distinctfile1)))
fname1.close()        

fname2.write(str('\n'.join(distinctfile2)))
fname2.close()  
