#write a program that read a number between 100 and 999 and print every part of it 


number = int(input('Chose a number between 100 and 999: '))
num = str(number)

if number >= 100 and number <= 900:
    print(num[0])
    print(num[1])
    print(num[2])

else:
    print('ERROR')
    print('Insert a number betwwen 100 and 999')