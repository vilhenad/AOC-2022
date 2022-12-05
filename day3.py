items=open("d3.txt").read().split("\n")
three=(list(set.intersection(*map(set,m)))[0] for m in (items[i:i + 3] for i in range(0, len(items), 3)))
both=(list(set(sack[:len(sack)//2]).intersection(set(sack[len(sack)//2:])))[0] for sack in items)
f=lambda m: (sum(map(lambda x: ord(x)-96 if "a"<=x<="z" else ord(x)-38,m)))
print(f(both)) # part 1
print(f(three)) # part 2