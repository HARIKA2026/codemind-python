n=str(int(input()))
a=list(n)
while (len(a)!=1):
    a=sum([int(i) for i in a])
    a=list(str(a))
print (a[0])      