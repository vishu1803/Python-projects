import random

# Guess the number from computer

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be High b/c Low = High
        feedback = input(f'Is {guess} too high (H), too Low (L), or correct (C)?? ').Lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low =guess + 1
    print (f'Yay! The computer guessed your number, {guess}, correctly!!')