def separate(file):
    with open(file) as f:
        for line in f.read().split('\n'):
            print(line.split('\t')[-1])

filename = input('분리할 파일명을 확장명과 함께 입력해 주세요.')
print(separate("zh_en.txt"))