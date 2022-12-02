rules={1:2,2:3,3:1}
# 1 loose, 2 draw, 3 win
# 1 rock, 2 scissors, 3 paper
# all possiblitlies (previously calculated and then pasted)
dp1={(1, 1): 4, (1, 3): 3, (2, 1): 1, (2, 3): 9, (3, 3): 6, (3, 2): 2, (2, 2): 5, (3, 1): 7, (1, 2): 8}
dp2={(1, 1): 3, (1, 3): 8, (2, 1): 1, (2, 3): 9, (3, 3): 7, (3, 2): 6, (2, 2): 5, (3, 1): 2, (1, 2): 4}
tot1=0
tot2=0
for line in open("d2.txt"):
    if line!="\n":
        t=tuple(map(lambda x: ord(x)-64 if ord(x)<=67 else ord(x)-23-64,line.strip().split(" ")))
        tot1+=dp1[t]
        tot2+=dp2[t]
print(tot1,tot2)