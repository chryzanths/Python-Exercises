secret_word = "hoshi"
guess = input("Guess a word: ")
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    guess_count += 1
    if guess_count < guess_limit:
        print("Wrong! Try again!")
        guess = input("Guess again: ")
    else:
        out_of_guesses = True

if out_of_guesses:
    print("out of guesses")
else:
    print("You've guessed it! Congrats!")

