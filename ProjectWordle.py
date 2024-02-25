correct1 = "car"
correct2 = "pie"
word1 = False
word2 = False
guess = ""
guess_counter = 0

fc = input("Hello what type of word would you like to guess? \n You can choose between food and vehicle")
if fc == "food":
  word2 = True
elif fc == "vehicle"
  word1 = True
while word1 == True:
  while guess != correct1:
    guess = input("Guess the word: ")
    if guess != correct1:
      print("Wrong answer! Try again")
      guess_counter = guess_counter + 1
    else:
      print("Congratulations!")
      print("You guessed the word in just " + str(guess_counter) + " guesses :D")

while word2 == True:
  while guess != correct2:
    guess = input("Guess the word: ")
    if guess != correct2:
      print("Wrong answer! Try again")
      guess_counter = guess_counter + 1
    else:
      print("Congratulations!")
      print("You guessed the word in just " + str(guess_counter) + " guesses :D")
