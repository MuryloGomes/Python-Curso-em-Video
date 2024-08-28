numero_inteiro = int(input('Digite um número inteiro: '))

base_de_conversao = int(input("""Digite 1 para converter o número para binário
Digite 2 para octal
Digite 3 para hexadecimal"""))

if base_de_conversao == 1:
    print('Seu número foi convertido para binário')

elif base_de_conversao == 2:
    print('Seu número foi convertido para octal')

elif base_de_conversao == 3:
    print('Seu número foi convertido para hexadecimal')