#Write a program that reads n complete numbers and the print the odd numbers


n = int(input('Chose n: '))
oddnum = []
par = 0

for numero in range(n):
    numbers = float(input('Insert {} numbers here: '.format(n)))
    if (numbers%2) != 0:
        oddnum.append(numbers)   
    else:
        oddnum.append(numbers)
        oddnum.pop()
        

print('{}It´s an odd number'.format(oddnum))
