import random
import startAnimation
import checkAnimation
import title
import sys
import os

#if os.name == "nt":
#    os.system("cls")
#else:
#    os.system("clear")
try:
    startAnimation.starting_animation()

    sys.stdout.write(title.title())

    ball_Box = random.randint(1,3)
    user_Guess1 = int(input("\n Tell me your guess [1] or [2] or [3]....."))
    checkAnimation.checking_animation()

    sys.stdout.write(title.title())

    if ball_Box == user_Guess1:
        sys.stdout.write("\n You won!,Your guess is correct")
    else:
        sys.stdout.write("\n ooh no, its a wrong guess")
        user_Guess2 = int(input("\n this is the last try...    "))
        checkAnimation.checking_animation()

        sys.stdout.write(title.title())

        if user_Guess2 == ball_Box:
            sys.stdout.write("\n your guess is correct this time")
        else:
            sys.stdout.write("\n you lose, no more tries left")
except:
    sys.stdout.write("\n enter a valid response")
