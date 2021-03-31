line1 = []
line2 = []
def separate(file):
    with open(file) as f:
        for line in f.read().split('\n'):
            line1.append(line.split('\t')[0])
            line2.append(line.split('\t')[-1])

separate(input('분리할 파일명을 확장명과 함께 입력해 주세요 '))

file1 = open(input('첫번째 열의 데이터를 저장할 파일명을 확장명과 함께 입력해 주세요 '), 'w')
file2 = open(input('두번째 열의 데이터를 저장할 파일명을 확장명과 함께 입력해 주세요 '), 'w')

file1.write(str('\n'.join(line1)))
file2.write(str('\n'.join(line2)))
file1.close()
file2.close()