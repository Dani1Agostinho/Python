#write a program that reads 10 numbers, and show the biggest and the smalest 


lista = []


for algo in range(1, 11):
    num = input('Insert the numbers :')
    lista.append(num)
    
print('The biggest number is {} and the lowest is {}'.format(max(lista), min(lista)))


    
    
