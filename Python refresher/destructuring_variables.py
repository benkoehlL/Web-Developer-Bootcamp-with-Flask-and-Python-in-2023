t = 5, 11
x, y = t

print(x,y)

student_attendence = {"Benjamin": 100, "Peter": 78, "Silvia": 98}
for t in student_attendence.items():
    print(t)

for student, attendence in student_attendence.items():
    print(student, '\t', attendence)

head, *tail = [1,3,4,5,7]
print(head,'\t', tail)
*head, tail = [1,3,4,5,7]
print(head,'\t', tail)