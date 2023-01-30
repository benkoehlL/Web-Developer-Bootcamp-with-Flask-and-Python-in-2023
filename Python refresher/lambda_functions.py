def add(x,y):
    return x+y

print(add(1,2))

add = lambda x,y: x+y

print(add(5,7))

print((lambda x,y: x+y)(5,9)) # very uncommon use

def double(x):
    return 2*x

sequence = [1,2,4,9]
doubled = [double(x) for x in sequence]
print(doubled)

doubled_map = list(map(lambda x : 2*x, sequence))
print(doubled_map)