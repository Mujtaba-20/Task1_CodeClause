import random
i=1
guess = random.randint(1,99)
print("="*100)
print("Number Guessing Game")
print("“Your instincts vs my randomness. Can you crack it?”")
print("="*100)
while i <= 3:
    num = int(input("Enter your guess: "))
    i+=1
    if num == guess:
        print("You guessed it right!")
        break
    elif num > guess:
        print("Guessed number too high!")
    elif num < guess and num > 0:
        print("Guessed number too low!")
    elif num <= 0:
        print("Guess a positive number!")
    
if num != guess:
    print("You Lost!")
