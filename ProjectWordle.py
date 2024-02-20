correct = "pie"
guess = ""
guess_counter = 0

while guess != correct:
  guess = input("Guess the word: ")
  if guess != correct:
    print("Wrong answer! Try again")
    guess_counter = guess_counter + 1
  else:
    print("Congratulations!")
print("You guessed the word in just " + str(guess_counter) + " guesses \o/!")
