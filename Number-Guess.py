import random

mys_num = random.randint(1, 30)
guess_left = 5
count = 0

print(" ")

name = input("Hi there! What's your name?\n"
             "You: ")

print(" ")

yes_no = input("Ok " + name + ", let's play a 'number-guessing' game?\n"
               "" + name + ": ")

print(" ")
print(" ")
print(" ")
print("Let's play then!")
print("You will have 5 guesses, within 5 guesses you should get the number.\n"
      "If you don't, you will loose!")
print(" ")

print("Ok let's start!")
print("I am thinkig of a number between 1 and 30. What's the number " + name + "?")


while guess_left != 0:

    print("You have " + str(guess_left) + " guess left.\n"
          "What is your guess?")

    your_guess = input("" + name + ": ")

    if int(your_guess) > mys_num:
            print(" ")
            print("It's a bit too high.")
            print(" ")
            guess_left -= 1
            count += 1

    elif int(your_guess) < mys_num:
            print(" ")
            print("It's a bit too low.")
            print(" ")
            guess_left -= 1
            count += 1

    elif int(your_guess) == mys_num:
            count += 1
            print(" ")
            if count == 1:
                print("You guessed it right with just " + str(count) + " try!")
            else:
                print("You guessed it right with just " + str(count) + " tries!")
            print(" ")
            break
    else:
        print("Wrong Input, use a integer between 1 and 30.")

    if guess_left == 0:
            print(" ")
            print("Your guesses are over, good luck next time " + name + "!")
            print(" ")
            break
        
            
