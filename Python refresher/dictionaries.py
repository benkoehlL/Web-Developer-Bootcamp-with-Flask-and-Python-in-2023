## simple dictionaries
friend_ages = {"Rolf" : 24,
            "Benjamin": 32,
            "Flaubert": 120}

print(friend_ages["Benjamin"])

# add an element
friend_ages["Bob"] = 26
print(friend_ages)

# change an element
friend_ages["Benjamin"] = 33

print(friend_ages)

##higher order dictionaries
friends = [
    {"name": "Benjamin",
    "age": 32,
    "height": 186},

    {"name": "Paul",
    "age": 30,
    "height": 190},

    {"name": "Hans",
    "age": 19,
    "height": 175}
]

# access elements
print("all friends ", friends, '\n', "friend2 ", friends[1],'\n', "friend2's age ", friends[1]["age"])

student_attendence = {"Benjamin": 100, "Peter": 78, "Silvia": 98}
for student, attendence in student_attendence.items():
    print("student: {} \t attendence: {}".format(student, attendence))

print("The average attendence is ", sum(student_attendence.values())/len(student_attendence))