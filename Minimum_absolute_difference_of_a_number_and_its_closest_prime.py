def prime(a):
    for j in range(2,a):
        if(a%j==0):
            return False
    else:
        return True
a=int(input())
z=a
s1=0
s2=0
for k in range(a):
    a=a-1
    if prime(a):
        s1=a
        break
for m in range(a):
    a=a+1
    if prime(a):
        s2=a
        break
x=z-s1
y=s2-z
print(min(x,y))