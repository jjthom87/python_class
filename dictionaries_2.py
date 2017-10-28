students = {
		"Alice":["ID01",25,"A"],
		"Rob":["ID02",23,"B"], 
		"Rick":["ID03",25,"C"],
		"Pat":["ID04",22,"D"]
		}

print(students)

print(students["Pat"])
print(students["Rick"][0])
print(students["Pat"][1:])

students_two = {
		"Alice":{"id":1,"age":25,"grade":"A"},
		"Rob":{"id":2,"age":23,"grade":"B"}, 
		"Rick":{"id":3,"age":21,"grade":"C"},
		"Pat":{"id":4,"age":28,"grade":"D"}
		}

print(students_two)
print(students_two["Rob"]["age"])
print(students_two["Pat"]["id"],students_two["Pat"]["grade"])