def join(file1, file2):
    lines1 = []
    lines2 = []
    joined = []
    with open(file1) as f1:
        with open(file2) as f2:
            for line1 in f1.read().split('\n'):
                lines1.append(line1)
            for line2 in f2.read().split('\n'):
                lines2.append(line2)
    for i in range(len(lines1)):
        joined.append((lines1[i]+'\t'+lines2[i]))

    save = open(input("저장할 파일명을 확장명과 함께 입력해 주세요 "),'w')
    save.write(str('\n'.join(joined)))
    save.close()  

file_1 = input("병합할 첫번째 파일 명을 확장명과 함께 입력해 주세요 ")
file_2 = input("병합할 두번째 파일 명을 확장명과 함께 입력해 주세요 ")

join(file_1, file_2)