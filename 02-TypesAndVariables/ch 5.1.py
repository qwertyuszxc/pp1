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
sum = 0.0
print('total: '+str(len(list)))
for number in list:
    sum = sum + float(number)
print('sum: '+str(sum))
print('average: ' +str(sum / float(len(list))))