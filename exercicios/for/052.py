for c in range(1):
    numero = int(input('Digite um número inteiro: '))
    if numero % 1 == 0 and numero % numero == 0:
        print(f"O número {numero} é primo")
    else:
        print('O número não é primo')
