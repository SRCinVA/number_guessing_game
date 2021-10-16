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
print(random_number)

while True:
    user_guess = input("Make a guess: ")
    input != random_number

    if user_guess.isdigit():
    user_guess = int(user_guess)

    if user_guess <= 0:
        print("Please type out a number larger than 0 next time.")
        quit()
    else:
        print("Need an actual number, my friend.")
        quit()




    print("Sorry, dude ...")
    break 