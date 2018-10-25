import random

min = int(input("Choose the lowest number in the range: "))
max = int(input("Choose the highest number in the range: "))

def new_game():

    # Initial variables
    current = random.randrange(min,max)
    all_vals = [current]
    alive = True
    score = 0

    print("The first number is " + str(current))

    while alive:

        print("Numbers so far: " + str(all_vals))
        user_ans = input("Will the next number be Higher or Lower: (enter H/L) ")

        value_found = False
        next_val = random.randrange(min, max) # Get the next number

        # Keep getting new numbers until a unique number is pulled, add these to the table of numbers pulled
        while not value_found:
            if next_val not in all_vals:
                all_vals.append(next_val)
                value_found = True
            else:
                next_val = random.randrange(1,11)

        # Case 1: User guesses high
        if user_ans.lower() in {"hi", "high", "h", "higher"}:
            if next_val > current:
                current = next_val
                print("Number drawn is: " + str(current) + ". You got it right!")
                score = score + 1
            else:
                current = next_val
                print("Number drawn is: " + str(current) + ". You got it wrong..")
                alive = False

        # Case 2: User guesses low
        elif user_ans.lower() in {"low", "lo", "l", "lower"}:
            if next_val < current:
                current = next_val
                print("Number drawn is: " + str(current) + ". You got it right!")
                score = score + 1
            else:
                current = next_val
                print("Number drawn is: " + str(current) + ". You got it wrong..")
                alive = False

        # Case 3: User enters an invalid option
        else:
            print("Option not recognised, please enter H for high or L for low..")

    # Display users score and ask if they'd like to play again
    print("Your score was: " + str(score))
    choice = input("Would you like to play again? (Y/N) ")
    if choice.lower() in {"yes", "y", "ya"}:
        new_game()
    else:
        print("Thanks for playing!")

# Get things started
new_game()