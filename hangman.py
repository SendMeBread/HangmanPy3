import random
from pathlib import Path

def load_word():
	words_path = Path(__file__).with_name("words.txt")
	try:
		words = [line.strip().upper() for line in words_path.read_text(encoding="utf-8-sig").splitlines()
				 if line.strip()]
	except OSError as error:
		raise SystemExit(f"Unable to read {words_path}: {error}")
	if not words:
		raise SystemExit(f"No words found in {words_path}.")
	return random.choice(words)


def play():
	word = load_word()
	guessed_letters = set()
	incorrect_guesses = set()
	allowed_misses = 6

	print("Welcome to Hangman!")
	while True:
		display = " ".join(
			character if character == " " or character in guessed_letters else "_"
			for character in word
		)
		print(f"\n{display}")
		if incorrect_guesses:
			print("Incorrect guesses:", " ".join(sorted(incorrect_guesses)))
		print(f"Misses remaining: {allowed_misses - len(incorrect_guesses)}")

		if all(character == " " or character in guessed_letters for character in word):
			print("You won!")
			return
		if len(incorrect_guesses) == allowed_misses:
			print(f"You lost. The word was {word}.")
			return

		guess = input("Guess a letter: ").strip().upper()
		if len(guess) != 1 or not guess.isalpha():
			print("Enter a single letter.")
		elif guess in guessed_letters or guess in incorrect_guesses:
			print("You already guessed that letter.")
		elif guess in word:
			guessed_letters.add(guess)
			print("Correct!")
		else:
			incorrect_guesses.add(guess)
			print("That letter is not in the word.")


if __name__ == "__main__":
	play()