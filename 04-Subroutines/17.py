x = float(input('Input X coordinate: '))
y = float(input('Input Y coordinate: '))
if x > 0 and y > 0:
 print(f'Point P({x},{y}) is in the first quadrant')
elif x < 0 and y < 0:
 print(f'Point P({x},{y}) is in the third  quadrant')
elif x < 0 and y > 0:
 print('fPoint P({x},{y}) is in the second quadrant')
elif x > 0 and y < 0:
 print(f'Point P({x},{y}) is in the fourth quadrant')
elif x == 0 and y == 0:
 print(f'Point P({x},{y}) is in the 0,0')