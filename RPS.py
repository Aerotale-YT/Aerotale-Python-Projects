
# RTC_1""34@$%£eeRg||-+}}[~

import random

point_a = 0
point_b = 0
round_ = 0

react = random.randint(1, 3)

print(' ')
print("Let us play Rock, Paper, Scissor!")
print(' ')
_round = int(input('How many rounds rounds you want to play?\n'
                   ': '))

print("There will be " + str(_round) + " rounds\n"
      "Those who win the most matches will be the winner\n"
      " ")

# Mainloop

while round_ <= _round:

    inter_a = input("[R]ock/[P]aper/[S]cissor\n"
                    "You: ")

    if react == 1:
        react = 'r'
    if react == 2:
        react = 'p'
    elif react == 3:
        react = 's'

    if inter_a.lower() == react:
        if react == 'r':
            print('Comp: Rock')
        elif react == 's':
            print('Comp: Scissor')
        elif react == 'p':
            print('Comp: Paper')
        round_ += 0
        print(' ')
        print("Let us repeat.")
        print(round_, "round(s) are over")
        print(' ')
        react = random.randint(1, 3)

    # Loosing

    elif inter_a.lower() == 'r' and react == 'p':
        if react == 'r':
            print('Comp: Rock')
        elif react == 's':
            print('Comp: Scissor')
        elif react == 'p':
            print('Comp: Paper')
        point_b += 1
        round_ += 1
        print(' ')
        print("You lost this, your opponent got 1 more point.")
        print(round_, "round(s) are over")
        print(' ')
        react = random.randint(1, 3)

    elif inter_a.lower() == 'p' and react == 's':
        if react == 'r':
            print('Comp: Rock')
        elif react == 's':
            print('Comp: Scissor')
        elif react == 'p':
            print('Comp: Paper')
        point_b += 1
        round_ += 1
        print(' ')
        print("You lost this, your opponent got 1 more point.")
        print(round_, "round(s) are over")
        print(' ')
        react = random.randint(1, 3)

    elif inter_a.lower() == 's' and react == 'r':
        if react == 'r':
            print('Comp: Rock')
        elif react == 's':
            print('Comp: Scissor')
        elif react == 'p':
            print('Comp: Paper')
        point_b += 1
        round_ += 1
        print(' ')
        print("You lost this, your opponent got 1 more point.")
        print(round_, "round(s) are over")
        print(' ')
        react = random.randint(1, 3)

    # Winning

    elif inter_a.lower() == 'p' and react == 'r':
        if react == 'r':
            print('Comp: Rock')
        elif react == 's':
            print('Comp: Scissor')
        elif react == 'p':
            print('Comp: Paper')
        point_a += 1
        round_ += 1
        print(' ')
        print("You won this, you got 1 more point.")
        print(round_, "round(s) are over")
        print(' ')
        react = random.randint(1, 3)

    elif inter_a.lower() == 's' and react == 'p':
        if react == 'r':
            print('Comp: Rock')
        elif react == 's':
            print('Comp: Scissor')
        elif react == 'p':
            print('Comp: Paper')
        point_a += 1
        round_ += 1
        print(' ')
        print("You won this, you got 1 more point.")
        print(round_, "round(s) are over")
        print(' ')
        react = random.randint(1, 3)

    elif inter_a.lower() == 'r' and react == 's':
        if react == 'r':
            print('Comp: Rock')
        elif react == 's':
            print('Comp: Scissor')
        elif react == 'p':
            print('Comp: Paper')
        point_a += 1
        round_ += 1
        print(' ')
        print("You won this, you got 1 more point.")
        print(round_, "round(s) are over")
        print(' ')
        react = random.randint(1, 3)
    else:
        print("Wrong Input; 'R' is for Rock, 'P' is for Paper, 'S' is for Scissor\n"
              " ")

    if round_ == _round:
        if point_a > point_b:
            print(' ')
            print(' ')
            print('You won the entire match!! You got ' + str(point_a) + ' point(s).\n'
                  'Your opponent got ' + str(point_b) + ' point(s).')
            break
        elif point_b > point_a:
            print(' ')
            print(' ')
            print('You lost the entire match!! You got ' + str(point_a) + ' point(s).\n'
                  'Your opponent got ' + str(point_b) + ' point(s).')
            break
        elif point_a == point_b:
            print(' ')
            print(' ')
            print('It is a draw.\n'
                  'Your opponent got ' + str(point_b) + ' point(s).\n'
                                                        'You got ' + str(point_a) + ' point(s).')
            break
