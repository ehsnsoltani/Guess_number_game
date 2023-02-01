import random
import art
# creating a list of numbers from 1 to 100 using List and For Loops
numbers = []
for x in range(1, 101):
    numbers.append(x)

# selectin a number from numbers list randomly using choice and random module
num_selected = random.choice(numbers)


#difining easy and hard level of game 
HARD_LEVEL = 5
EASY_LEVEL = 10
game_level = 0



#selecting game level depends on user input
def level():
    global game_level
    if selected_level == "hard":
        game_level = HARD_LEVEL
        return game_level
    else:
        game_level = EASY_LEVEL
        return game_level





#checking if user guessed number is correct or not
def check_guess():
    if user_guess == num_selected:
        return True
    else:
        return False

#showing user how far or low is from selected num from 1 to 100
def low_high():
    if user_guess > num_selected:
        print("too high")
    else:
        print("too low")



print("Wellcom to the Number Guessing Game\nI'm thinking of a number between 1 and 100")
print(num_selected)
selected_level = input("Select your Game Level: 'hard' or 'easy': ")
level()
print(f"you have {game_level} attempts remaining to guess the number.")


# a flag for while loop
continue_game = True
while continue_game:
    user_guess = int(input("Make a guess: "))
    if check_guess():
        continue_game = False
        print("you guess rigth!")
    else:
        game_level -= 1
        if game_level == 0:
            continue_game = False
            print("you've run out of guesses, you lost!")
        else:
            low_high()
            print("Try again")
            print(f"you have {game_level} attempts remaining to guess the number.")
