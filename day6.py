text = open("d6.txt").read().strip()
m = lambda n: next(filter(lambda i: len(set(text[i:i+n]))==n, range(len(text)-n)))+n # next acts as a break
print(m(4)) # part 1
print(m(14)) # part 2