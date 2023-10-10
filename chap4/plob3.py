import random as rd
print("           Welcome to 'Guess My Number'!       ")
print("I'm thinking of a number between 1 and 100")
print("Try to guess it in as few attenpts as possible.")
num = rd.randint(1,100)
i = 0
j = 0

while j != num:
    i += 1
    j = int(input("Take a guess: "))
    
    if j < num:
        print("Lower....")
    elif j > num:
        print("Higher....")
    elif j == num:
        print("You guessed it! The number was", num)
        print("And it only took", i, "tries!")
