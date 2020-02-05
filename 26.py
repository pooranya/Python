a=list(map(int,input()))
b=sum(a)
if len(a)>=2:
    print(b**len(a))
else:
    print(b)
