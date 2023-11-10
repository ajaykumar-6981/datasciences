

l=[1,2,3]
l.append(4)

print(l)

l.count(10)
print(l.count(10))

print(l.count(1))

x=[1,2,3]
x.append([4,5])

print(x)

x.extend([4,5,6])
print(x)

print(l.index(1))

l.insert(2,'inserted')
print(l[2])
print(l)

ele=l.pop()
print(ele)
print(l)

l.remove('inserted')
print(l)

l.sort()
print(l)