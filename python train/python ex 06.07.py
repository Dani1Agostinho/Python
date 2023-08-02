

#Write a program that do the average of 10 positive numbers and ignore the negative numbers

acum = 0
count = 0
positive = 0


while count < 4:
    acum = acum + float(input('Insert a value: '))
    count += 1
    for num in list[acum]:
        if num >= 0:
            positive += 1
   
        