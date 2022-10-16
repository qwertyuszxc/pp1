hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
    if float(hours) > 40:
        over = float(hours) - 40
        payment = ((float(hours)-over)*float(rate)) +(over * (float(rate)*1.5))
    else: 
        payment = float(hours)*float(rate) 
except:
    print('Please,input numbers')
else:
    print('Pay ' + str(payment))