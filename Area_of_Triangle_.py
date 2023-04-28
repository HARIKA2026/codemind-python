import math
A,B,C=map(int,input().split())
S=(A+B+C)/2
p=S*(S-A)*(S-B)*(S-C)
Area=math.sqrt(p)
print("%.2f"%Area)