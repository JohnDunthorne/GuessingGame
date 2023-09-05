# These are attributes
secret_number = 9
number_of_guesses = 0
Number_of_lives = 3
print("Guess a number from 1 - 100, you get three tries")
# While statement here controls what happens based on a number of guesses made
# it increments the number of guesses by 1 everytime an incorrect guess is made
while number_of_guesses < Number_of_lives:
    guess = int(input("Guess: "))
    number_of_guesses += 1
# this statement means guess is NOT equal to the secret number
# AND the number of guesses made is equal to 1
    if guess != secret_number and number_of_guesses == 1:
        print("2 more chances")
    if guess != secret_number and number_of_guesses == 2:
        print("1 more chance")
# break happens when correct answer is made, so while loop doesn't continue
    elif guess == secret_number:
        print("Winner!")
        break
# else takes effect when number of guesses is no longer less than number of lives
else:
    print("You ran out of lives")