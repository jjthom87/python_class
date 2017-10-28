for number in range(1,11):
	print(number)

for number in range(1,30,3):
	print(number)

for letter in "abcd":
	print(letter)

vowels = 0
consonants = 0
capitals = 0

for letter in "Hello i love you wont you tell me your name":
	if letter.lower() in "aeiou":
		vowels = vowels + 1
	elif letter == " ":
		pass
	elif not letter == letter.lower():
		capitals = capitals + 1
	else:
		consonants = consonants + 1

print("Consonants: {}".format(consonants))
print("Vowels: {}".format(vowels))
print("Capitals: {}".format(capitals))