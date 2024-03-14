import random; 



def numGame(mini, maxi, tries, hints):
    randomNum = random.randint(mini, maxi)
    print(f"Random number between {min} & {maxi} was selected, you have {tries} tries. ")
    print("Good luck! \n")

    while tries >= 0:
        guess = None
        while guess is None:
            try:
                guess = int(input(" -> "))
            except(ValueError):
                guess = None
                print("not a valid number! ")

        if hints:
            if guess == randomNum:
                print(f"{guess} is the correct number! ")
                print("Congrats you win. ")
                print(f"You had {tries-1} tries left, with hints. ")
                break
            elif guess >= randomNum:
                print("I'm sorry but that is incorrect. :) You should aim lower. ")
                tries -= 1
            elif guess <= randomNum:
                print("I'm sorry but that is incorrect. :) You should aim higher. ")
                tries -= 1
        else:
            if guess == randomNum:
                print(f"{guess} is the correct number! ")
                print("Congrats you win. ")
                print(f"You had {tries-1} tries left, with no hints! ")
                break
            elif guess != randomNum:
                print("I'm sorry but that is incorrect. :) ")
                tries -= 1

    if tries == 0:
        print(f"You didn't guess the number, it was {randomNum}. ")