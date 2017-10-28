from random import choice

questions = ["Why is the sky blue?: ", "What is a rock?: ", "Where are the dinosaurs?: "]
question = choice(questions)
answer = input(question).lower()

while answer != "just because":
	answer = input("why?: ").strip().lower()

print("Oh Okay")

