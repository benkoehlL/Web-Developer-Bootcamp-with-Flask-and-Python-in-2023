from operator import itemgetter

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend/divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(1,2, operator=divide)
print(result)

def search(sequence, expected, finder):
    for elem in sequence:
        if(finder(elem) == expected):
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Dina Ivanova", "age": 32},
    {"name": "Benjamin Köhler", "age": 32},
    {"name": "Hans Meiser", "age": 72}
]

def get_friend_name(friend):
    return(friend['name'])

try:
    for i in ["Dina Ivanova", "Jan Ulrich"]:
        friend = search(friends, i, get_friend_name)
        print(friend)
    
except RuntimeError as e:
    print(e)

try:
    for i in ["Dina Ivanova", "Jan Ulrich"]:
        friend = search(friends, i, lambda friend : friend['name'])
        print(friend)
    
except RuntimeError as e:
    print(e)

try:
    for i in ["Dina Ivanova", "Jan Ulrich"]:
        friend = search(friends, i, itemgetter('name'))
        print(friend)
    
except RuntimeError as e:
    print(e)