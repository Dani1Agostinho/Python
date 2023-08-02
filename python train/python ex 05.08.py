


Salario = float(input('What´s your month payment: '))
empres = float(input('what is the value of the loan: '))

if empres < Salario*20//100:
    print('The loan was complete')
else:
    print('The loan can not be completed ')