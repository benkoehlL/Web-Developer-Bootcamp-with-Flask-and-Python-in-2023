list = ["Benjamin", "Rolf", "Anne"]  # can be modified (elements can be added and removed)
tuple = ("Benjamin", "Rolf", "Anne") # can not be modified
set = {"Benjamin", "Rolf", "Anne"}   # can not have duplicate elements and order is not guaranteed, but can be modified 

print(list[0]) # print first element
print(list[0:2]) # print first two elements
print(tuple[0]) # print first element
print(tuple[0:2]) # print first two elements
## above is impossible for sets

list[0] = "God" # impossible for tuples and sets
print(list)
list.append("Hans") # impossible for tuples
print(list)
list.remove("Rolf")
print(list)

set.add("Hans") # as sets do not have an end to append to, the function to add an element is add :)
set.add("Hans") # this does nothing as sets can not contain duplicates
print(set)