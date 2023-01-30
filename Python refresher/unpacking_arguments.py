def multiply(*args):
    print(args)
    total = 1
    for factor in args:
        total = total*factor
    return total

def add(x,y):
    return(x+y)

l = [1, 2, 5, 7]
print(multiply(1, 2, 5, 7))
nums = [3,5]
print(add(*nums))

nums = {"x": 3, "y": 5}
print(add(**nums))

def apply(*args, operator):
    if operator == '*':
        return multiply(*args)
    elif operator == '+':
        return sum(args)
    else:
        return "No valid operator provided to apply()."
l = [1, 2, 5, 7]

print("add: ", apply(*l,operator='+'),'\n', "multiply: ", apply(*l,operator='*'))
print(apply(1,3,5,6,operator='+'),'\n', apply(1,3,5,6,operator='*'))