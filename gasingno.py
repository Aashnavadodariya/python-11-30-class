import random
num=random.randint(1,20)

while True:
    guess=int(input("guess a number between 1 to 20 :"))
    if guess==num:
        print("you guessed a correct number")
        break
    elif guess>num:
        print("you guessed a greter number")
    elif guess<num:
        print("you guessed a smaller no")
