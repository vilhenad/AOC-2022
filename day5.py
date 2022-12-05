from collections import deque # for O(1) but could use lists, O(n), for popping and appending
stacks=[
    deque(["R","G","J","B","T","V","Z"]),\
    deque(["J","R","V","L"]),\
    deque(["S","Q","F"]),\
    deque(["Z","H","N","L","F","V","Q","G"]),\
    deque(["R","Q","T","J","C","S","M","W"]),\
    deque(["S","W","T","C","H","F"]),\
    deque(["D","Z","C","V","F","N","J"]),\
    deque(["L","G","Z","D","W","R","F","Q"]),\
    deque(["J","B","W","V","P"])
    ] # cba to parse the stacks :)
stacks2=[s.copy() for s in stacks] # deep copy
moves = eval(open("d5.txt").read().replace("move ","[").replace(" from ",",").replace(" to ",",").replace("\n","],")+"]") # eval magic :)
for move in moves:
    (stacks[move[2]-1].append(stacks[move[1]-1].pop()) for _ in range(move[0])) # part 1
    stacks2[move[2]-1].extend([stacks2[move[1]-1].pop() for _ in range(move[0])][::-1]) # part 2
print("".join([i.pop() for i in stacks])) # part 1
print("".join([i.pop() for i in stacks2])) # part 2

