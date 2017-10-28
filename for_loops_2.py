students = {
	"Jared": {"id": 1, "age":30, "eye_color": "blue"},
	"Joey": {"id": 2, "age": 31, "eye_color": "green"},
	"Jimmy": {"id": 3, "age": 26, "eye_color": "grey"}
}

for student in students:
	if "a" in student:
		print(student)

for key in students.keys():
	if students[key]['age'] >= 30:
		print(students[key])


students_two = {
	"males": ["Bob", "Chris", "Steve"],
	"females": ["Taylor", "Robyn", "Jamie"]
}