import itertools
inp=[[int(r) for r in i] for i in (map(list,open("d8.txt").read().split("\n")))]
grid={}
for lin, col in itertools.product(range(len(inp)), range(len(inp[0]))):
        grid[col,lin] = inp[lin][col]
col_arr = lambda c: ([grid[(c[0],i)] for i in range(c[1]-1,-1,-1)],[grid[(c[0],i)] for i in range(c[1]+1,len(inp))])
row_arr = lambda c: ([grid[(i,c[1])] for i in range(c[0]-1,-1,-1)],[grid[(i,c[1])] for i in range(c[0]+1,len(inp))])
valid=lambda c: 1<=c[0]<=len(inp[0])-2 and 1<=c[1]<=len(inp)-2 # not on border

def can_see(c): # part 1
    return any(
        all(map(lambda i: i < grid[c], arrs))
        for arrs in col_arr(c) + row_arr(c))

def score(c): # part 2
    m=1
    for arr in col_arr(c) + row_arr(c):
        i=0
        while arr[i]<grid[c] and i!=len(arr)-1:
            i+=1
        m*=(i+1)
    return m

part1=2*len(inp)+(2*(len(inp[0])-2)) # borders
part2=0
for cord in grid:
    if valid(cord):
        part2=max(part2,score(cord))
        if can_see(cord):
            part1+=1

print(part1,part2)
