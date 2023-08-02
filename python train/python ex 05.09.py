


altura = float(input('What is your height: '))
peso = float(input('What is your weight: '))
gender = input('Are you a Male or a Female: ')

if gender == 'male' or gender == 'Male':
    print(72.7 * altura - 58)
    print('This is the ideal weight')
elif gender == 'female' or gender == 'Female':
    print(62.1*altura - 58)
    print('This is the ideal weight')
