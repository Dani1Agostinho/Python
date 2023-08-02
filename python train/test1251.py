


posSum = 0

print("Please Enter 10 Numbers to Find Positive \n")
for i in range(1, 4):
    num = int(input("Number %d = " %i))

    if num < 0:
        continue

    posSum = posSum + num

print("The Sum of 10 Numbers by Skipping Negative Numbers = ", posSum)

