original = input("Please enter a sentence: ").strip().lower()

words = original.split()

new_words = []

for word in words:
	if word[0] in "aeiou":
		new_words.append(word + "yay")
	else:
		#split = list(word)
		#first_letter = split[0]
		#split.remove(split[0])
		#joined = "".join(split)
		#joined = joined + first_letter + "ay"
		#new_words.append(joined)
		vowel_pos = 0
		for letter in word:
			if letter not in "aeiou":
				vowel_pos = vowel_pos + 1
			else:
				break
			cons = word[:vowel_pos]
			the_rest = word[vowel_pos:]
			new_word = the_rest + cons + "ay"
			new_words.append(new_word)

print(" ".join(new_words))