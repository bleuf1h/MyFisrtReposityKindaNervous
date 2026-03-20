import random

try:
    number = random.randint(1, 70)
    attempts = 0
    maxattempts = 5
    print("You have five attempts")
    while attempts < maxattempts:
        guess = int(input("Guess a number from 1 to 70: "))
        attempts += 1

        if guess == number:
            print("WITCH!!!!!")
            break  
        elif guess > number:
            print("Too High")
        else:
            print("Too Low")
    else:
        print(f"No more attempts for u The number was {number}.")

except ValueError:
    print("THAT'S NOT A NUMBER VRO")
except Exception as e:
    print("Something went wrong", e)