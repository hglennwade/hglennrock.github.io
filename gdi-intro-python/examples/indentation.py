raw_input = input('Please enter a number: ')
#For Python 2.7, replace line 1 with:
#raw_input = raw_input('Please enter a number')
x = int(raw_input)
if x == 5:
    print('x is equal to 5')
    x_is_5 = True
    print('Still in the x == 5 block')
else:
    print('x is not equal to 5')
    x_is_5 = False
    print('Still in the else block of x == 5')
print('Outside of the if or else blocks.')
print('x_is_5:')
print(x_is_5)