# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
from http.client import responses


def int_check(question, low=None, high=None, exit_code=None):
    while True:
        response = input(question)

        if exit_code is not None and response == exit_code:
            return response

        try:
            response = int(response)
        except ValueError:
            print("Please enter a valid integer")

        if low is not None and response < low:
            print(f"The number can't be less than {low}")

        if high is not None and response > high:
            print(f"The number can't be more than {high}")
        return response

# Guessing loop

# replace number below with random number between high / low values
secret = 7

# parameters that already exist in base game
low_num = 0
high_num = 10
guesses_allowed = 5

# set guesses used to zero at the start of each round
guesses_used = 0
already_guessed = []

guess = ""
while guess != secret and guesses_used < guesses_allowed:

    # ask the user to guess the number...
    guess =int_check("Guess: ", low_num, high_num,"xxx")

    # check that they don't want to quit
    if guess == "xxx":
        # set end_game to use so that outer loop can be
        end_game = "yes"
        break

    # check that guess is not a duplicate
    if guess in already_guessed:
        print(f"You've already guessed {guess}.  You've *still* used "
              f"{guesses_used} / {guesses_allowed} guesses")
        continue


    # if guess is not a duplicate, add it to the 'already guessed' list
    else:
        already_guessed.append(guess)

    # add one to the number of guesses used
    guesses_used += 1


    # compare the user's guess with the secret number set up feedback statement


    # if we have guesses left...
    if guess < secret and guesses_used < guesses_allowed:
        feedback = (f"Too law, please try a higher number "
                    f"You've used {guesses_used} / {guesses_allowed} guesses")
    elif guess > secret and guesses_used < guesses_allowed:
        feedback = (f"Too high, please try a lower number. "
                    f"You've used {guesses_used} / {guesses_allowed} guesses")

    # when the secret number is guessed, we have three different feedback
    #options (lucky / 'phew' / well done)
    elif guess == secret:

        if guesses_used == 1:
            feedback = "🍀🍀 Lucky!  You got it on the first guess. 🍀🍀"
        elif guesses_used == guesses_allowed:
            feedback = f"Phew！ You got it in {guesses_used} guesses."
        else:
            feedback = f"Well done! You guessed the secret number in {guesses_used} guesses"

    # if there are no guesses left
    else:
        feedback = "Sorry - you have no more guesses. You lose this round!"

    # print feedback to user
    print(feedback)

    # additional feedback (warn user that they are running out of guesses)
    if guesses_used == guesses_allowed - 1:
        print("\n💣💣💣 Careful - you have one guess left! 💣💣💣")

print()
print("End of round")






