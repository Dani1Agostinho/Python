

#Write a program that ask for 10 numbers and then do the average of them 

acum = 0
count = 0

while count != 10:
    acum = acum + float(input('Insert a value: '))
    count += 1
print(acum//10)

