def named(**kwargs): 
# double star collects the arguments and the values 
# and puts those into a dictionary
    print(kwargs)

def named_reverse(name, age):
    print(name, age)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print("{}: {}".format(arg,value))

def both(*args, **kwargs):
    print("The unnamed arguments are: ", args)
    print("The keyword argumenss are: ", kwargs)

named(name="Bob", age=25)

dict = {"name": "Bob", "age": 25}
named_reverse(**dict)
print_nicely(name='Bob', age=25, height=186)
both(1,2,3,4,5,6, name='Bob', age=25, height=186)

# print_nicely(**"Bob") # this does not work as the argument is no dictionary
# print_nicely(**None)  # this does not work as the argument is no dictionary
