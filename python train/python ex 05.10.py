


numb1 = float(input('Put the first number here: '))
numb2 = float(input('Put the second number here: '))
operation = int(input('Now chose an operation: (1)multiplication, (2)division, (3)addition and (4)subtraction: '))

if operation == 1:
    print('{0}*{1} = {2}'.format (numb1, numb2,numb1*numb2))
elif operation == 2:
    print('{}/{} = {}'.format(numb1,numb2, numb1//numb2))
elif operation == 3:
    print('{} + {} = {}'.format(numb1, numb2, numb1+numb2))
elif operation == 4:
    print('{} - {} = {}'.format(numb1, numb2, numb1-numb2))
else:
    print('Wrong please use (1)multiplication, (2)division, (3)addition and (4)subtraction')







