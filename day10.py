inp=eval(open("d10.txt").read().replace("noop","69696969").replace("addx","").replace("\n",",")) # get tuple of ints
cycle=1
c={}
tot=1
for ins in inp:
    c[cycle]=tot
    if ins==69696969:
        cycle+=1
    else:
        tot+=ins
        cycle+=2
for i in range(1,241):
    if i not in c:
        c[i]=c[i-1]
print(sum(c[i]*i for i in (20,60,100,140,180,220))) # part 1

crt=""
for idx,x in enumerate(dict(sorted(c.items())).values()):
    pos=idx%40
    crt += "█" if x in (pos+1,pos,pos-1) else " "
    if (idx+1)%40==0:
        crt+="\n"
print(crt) # part 2