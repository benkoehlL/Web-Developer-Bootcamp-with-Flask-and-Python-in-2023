a = []
b = a

print(id(a), '\t', id(b))

a.append(35)
print(a, '\t', b)

b = []
print(a, '\t', b)
