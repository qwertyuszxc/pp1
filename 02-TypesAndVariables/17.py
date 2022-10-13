from sys import int_info


height = float(input('Write down youre height in cm '))
height_feet = height / 30.84
height_inch = height_feet - int(height_feet)
print('I am '+ str(height) +' tall, i.e. '+ str(int(height_feet))+' feet and '+str(int(height_inch*12)) +' inches')