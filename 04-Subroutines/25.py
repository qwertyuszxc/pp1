a = int(input('Enter height: '))
b = int(input('Enter width: '))
print('*'*b)
for i in range(a-2):
    print('*' + ' ' * (b - 2) + '*')
print('*'*b)
