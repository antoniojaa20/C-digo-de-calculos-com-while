opção = 6

while opção != 5:
    valor1 = int(input('Digite um valor: '))
    valor2 = int(input('Digite outro valor: '))
    print()
    print('Olá escolha uma opção para calcular: ')
    print('Digite 1 para somar os 2 valores')
    print('Digite 2 para subtrair os 2 valores')
    print('Digite 3 para multiplicar os 2 valores')
    print('Digite 4 para saber qual é o maior')
    print('Digite 5 para sair')
    print()
    opção = int(input('Digite qual a sua opção: '))
    if opção == 1:
        soma = valor1 + valor2
        print('A soma dos valores é igaual à {}'.format(soma))
    elif opção == 2:
        if valor1 > valor2:
            subtração = valor1 - valor2
            print('A subtração dos valores é igual à {}'.format(subtração))
        elif valor1 < valor2:
            subtração = valor2 - valor1
            print('A subtração dos vaalores é igual à {}'.format(subtração))
    elif opção == 3:
        multiplicação = valor1 * valor2
        print('A multiplicação dos valores é igual à {}'.format(multiplicação))
    elif opção == 4:
        if valor1 > valor2:
            print('O {} é o maior'.format(valor1))
        if valor1 < valor2:
            print('O {} é o maior'.format(valor2))
print('FIM')
