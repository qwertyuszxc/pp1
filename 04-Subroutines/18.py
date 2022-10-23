cost = int(input('Enter the amount in PLN: '))
coin5 = cost//5
coin2 = (cost - 5*coin5)//2
coin1 = cost - 5*coin5 - 2*coin2
print(f'The amount of PLN {cost} in coins:  ')
print(f'5 zł - {coin5}')
print(f'2 zł - {coin2}')
print(f'1 zł - {coin1}')