students = {}
students = {"Alice":25, "Bob":27,"Rick":30}
print(students)
print(students["Alice"])

students["Alice"]=26
print(students["Alice"])

#delete student
del students["Bob"]

print(students.keys())
#print(students.keys()[0])
a = list(students.keys())
print(a)
print(a[1])
print(students.values())
print(list(students.values())[1:])

print(students.items())