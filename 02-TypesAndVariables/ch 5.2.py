list = []
while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    else:
        try:
            list.append(float(number))
        except:
            print('Invalid input')
max = 0
for number in list:
    if number > max:
        max = number
print('Maximal is: '+str(max))
for number in list:
    min = number
    if number < min:
        number = min
print('Minimal is: '+str(min))