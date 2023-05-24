a,b=map(int,input().split())
k=max(a,b)
while(True):
    if(k%a==0 and k%b==0):
        lcm=k
        break
    k+=1
print(lcm)