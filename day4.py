pair = lambda c,b: c.issubset(b) or b.issubset(c)
over = lambda c,b: bool(c.intersection(b))
m = [[set(range(int(l.split("-")[0]),int(l.split("-")[1])+1)) for l in n] for n in [i.split(",") for i in open("d4.txt").read().split("\n")]]
size = lambda f: sum(1 for _ in filter(lambda i: f(*i),m))
print(size(pair)) # part 1 
print(size(over)) # part 2