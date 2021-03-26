
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
    return str('\n'.join(joined))    
