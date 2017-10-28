#forever loop
#while True:
#	print("Hello")
num = 0
while num <= 10:
	if(num % 2 == 0):
		print("even {}".format(num))
	elif(not num % 2 == 0):
		print("odd {}".format(num))
	num = num + 1

L = []
while len(L) < 3:
	new_name = input("Please add name: ").strip().capitalize()
	L.append(new_name)
print("Sorry, list is full")
print(L)

