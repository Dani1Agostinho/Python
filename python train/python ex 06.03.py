

#escreva um programma que faça um contagem regressiva de 10 a 1 e no final fale boom 

contagem = 10

while contagem > 0:
    print(contagem)
    contagem -= 1
    if contagem == 0:
        print('BOOM')

