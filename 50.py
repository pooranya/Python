a="hello"
b=set(a)
print(b)
b.remove('e')
print(b)
b.discard('i')
print(b)
b.discard("o")
print(b)
c=b.pop()
print(c)
b.update(['b','c'])
print(b)
b.add("j")
print(b)
d=list(b)
print(d)
print(sorted(d))
e="hai"
f=set(e)
print(f)
print(b.difference(e))
print(b.union(e))
print(b.intersection(e))
