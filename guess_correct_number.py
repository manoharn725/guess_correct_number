import random

randNumber = random.randint(1,100)


userGuess=None
guesses=0
while(userGuess != randNumber):
    userGuess= int(input(f"userGuess the random number: "))
    guesses +=1 
    if(userGuess==randNumber):
        print("congrats you gussed right number!!!")
    else:
        if(userGuess<randNumber):
            print("sorry you guessed wrong number!!! please enter the larger number")
        else:
            print("sorry you guessed wrong numbber!!! please enter the smaller  number ")  


print(f"you guessed number in {guesses} guesses")             

with open ("highest.txt","r")as f:
    highest= int(f.read())

if(highest>guesses):
    print("you have braked last highestScore Record!!!")
    with open ("highest.txt","w")as f:
        f.write(str(guesses))