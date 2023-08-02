


num1 = float(input('Put the first number here: '))
num2 = float(input('Put the second number here: '))

if num1 > num2:
    print('The first number is the biggest')
    result1 = float(num1 - num2)
    print('And thats the diferrence betwhen them is %d' % result1)
else:
    print('The second number is the biggest')
    result2 = float(num2 - num1)
    print('And thats the diferrence betwhen them is %d' % result2)
