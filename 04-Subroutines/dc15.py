from mymath import *

guess = read_number()
random = generate_number()

if int(guess) == int(random):
    print('Your guess is right')
else:
    print('You`re wrong')

print(guess,random)