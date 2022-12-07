files={}
pos=[]
dirs=set()
for line in open("d7.txt").read().strip().split("\n"):
    line=line.split(" ")
    if line[0]=="$":
        if line[1]=="cd":
            if line[2]=="..":
                if len(pos) > 0:
                    pos.pop(-1)
            elif line[2]=="/":
                pos=[]
            else:
                pos.extend(line[2].split("/"))
    elif line[0] != "dir":
        files["/".join(pos+[line[1]])]=line[0]
    dirs.add("/".join(pos))
tots = {dir: sum(int(size) for file, size in files.items() if file.startswith(dir)) for dir in dirs}
print(sum(filter(lambda size: size<100000,tots.values()))) # part 1
print(min(filter(lambda size: size>=tots[""] - 40000000, tots.values()))) # part 2