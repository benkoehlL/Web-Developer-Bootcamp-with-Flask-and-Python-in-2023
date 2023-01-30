name = "Benjamin"
print(f"Hello, {name}")
name = "Rolf"
print(f"Hello, {name}")
 
greeting = "Hello, {}"
with_name = greeting.format("Benjamin")
print(with_name)
with_name = greeting.format("Rolf")
print(with_name) 