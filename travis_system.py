known_users = ["John", "Jared", "Bob", "Ray"];
L = [1,5,2,6,2,9];
print(len(known_users))

while True:
	print("Hi! my name is Travis")
	name = input("What is your name: ").strip();
	if name in known_users:
		remove = input("Would you like your name removed (y/n)? ")
		if(remove == "y"):
			known_users.remove(name)
			print(known_users)
	else:
		print("{} is not in the database".format(name))
		add_me = input("Would you like your name added (y/n)? ");
		if(add_me == "y"):
			known_users.append(name.title());
			print(known_users)