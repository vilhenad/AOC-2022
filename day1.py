ans=sorted(eval(open("d1.txt").read().replace("\n\n",",").replace("\n","+"))) # kekw
print(ans[-1],sum(ans[-3:]))