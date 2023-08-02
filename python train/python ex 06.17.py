#Write a program that reads an natural number n and the show the sum of the numbers

quant = int(input('How many numbers do you want to add ? : '))
lista = []
numbers = 0

for algo in range(quant):
    numbers += 1
    num = (float(input('Insert the {} number :'.format(numbers))))
    lista.append(num)
    
    
    
print('The biggest number is {} and the lowest is {}'.format(max(lista), min(lista)))







