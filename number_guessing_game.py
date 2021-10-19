import random

#r = random.randrange(-1, 10) # prints a random number with range parameters (exclusive of last number)
                                # (last number alone is the stop)
# print(r)

top_of_range = input("Type a number: ")

# we need to validate the input.
# because it will be entered as a string, it has to be cast as a string.
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type out a number larger than 0 next time.")
        quit()
else:
    print("Need an actual number, my friend.")
    quit()

random_number = random.randint(0,top_of_range) # the same as above, but this time it goes to 11 : )
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Need an actual number, my friend.")
        continue # unlike "break," "continue" brings us back to the top of the loop
                 # nothing will run after "continue" if this else statement is invoked
                 # if it isn't invoked, the while will unfold below.

    if user_guess == random_number:
        print("Correct!")
        break    # this pulls you out of the loop.
    else:
        if user_guess > random_number:
            print("a bit lower next time!")
        if user_guess < random_number:  # could have just done an 'else' here instead.
            print("a bit higher next time!")

print("You got it in", guesses, "guesses.") # w/commas, don't need spaces or to cast it as an int.


