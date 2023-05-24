a=int(input())
for i in range(a):
    n=int(input())
    t=n
    s=0
    while(n>0):
        r=n%10
        s=r+s*10
        n=n//10
    if(t==s):
        print(True)
    else:
        print(False)