original = input("Please enter a sentence: ").strip().lower()

words = original.split()

new_words = []

for word in words:
	if(word[0] in "aeiou"):
		new_words.append(word + "yay")
	else:
		split = list(word)
		first_letter = split[0]
		split.remove(split[0])
		joined = "".join(split)
		joined = joined + first_letter + "ay"
		new_words.append(joined)

print(" ".join(new_words))