from difflib import SequenceMatcher
from copy import deepcopy
def read_data_base():
    try:
        with open ("data.txt", "r") as fp:
            lines =fp.read().splitlines()
        return sorted(lines, key=len)
    except:
        return False

def main() :
    data = {}
    lines = read_data_base()
    print(len(lines))
    already = []
    if lines==False:
        return
    with open ("test.txt", "r") as fp:
            text =fp.read().splitlines()
    print(text)
    print(len(text))
    for line in lines:
        y=0
        size = len(line.split(" "))
        test_size = 3 if size <13 else size//2.5
        if line in already:
            # print("continued: "+line)
            # print()
            continue
        already.append(line)
        temp = []
        for i in lines:
            x=0
            for word in line.split(" "):
                if word.lower() in text:
                    continue
                if word in i.split(" "):
                    x+=1
            if x>=test_size:
                y+=1
                temp.append(i)
                already.append(i)


        data[line]=[y]
        data[line].extend(temp)
    # print(len(data))
    data = sorted(data.items(), key=lambda x:x[1], reverse=True)
    print(len(data))
    # print(data[0])
    # input()
    with open ("OOP.txt", "w") as fp:
        for lines,values in data:
            fp.write(lines)
            fp.write("\n")
            for v in values:
                if lines == v:
                    continue
                try:
                    int(v)
                    fp.write(f"Repeated: {v}")
                    fp.write("\n")
                    continue
                except:
                    pass
                fp.write(f"{v}")
                fp.write("\n")
            fp.write("\n")
            fp.write("\n")
if __name__== '__main__':
    main()