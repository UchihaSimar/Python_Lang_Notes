student = {
    "name":"Simar",
    "age":31,
    "courses":["Math", "Comp Sci"]
} # Keys can be any immutable data type like

print(student)
print(student["age"])
student['phone'] = '555555'
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone','NOT FOUND'))

