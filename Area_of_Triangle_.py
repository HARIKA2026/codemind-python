import math
A,B,C=map(int,input().split())
S=(A+B+C)/2
p=(S*(S-A)*(S-B)*(S-C))
ans=math.sqrt(p)
print("%.2f"%ans)