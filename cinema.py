films = {
	"Finding Dory": [3,5],
	"Shawshank Redemption": [20,5],
	"Fight Club": [12, 5],
	"It": [22,5]
}

while True:
	print(films)
	choice = input("What film would you like to watch?: ").strip().title()
	if choice in films:
		#pass
		age = int(input("How old are you?: ").strip())
		if age >= films[choice][0]:
			num_seats = films[choice][1]
			if num_seats > 0:
				print("Enjoy the film")
				#num_seats = num_seats - 1 does not work
				films[choice][1] = films[choice][1] - 1
			else:
				print("Sorry, all sold out")
		else:
			print("You are too young to see that film")
	else:
		print("We don't have that film")