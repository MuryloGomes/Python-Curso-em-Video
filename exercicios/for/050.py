variavel_acumuladora = 0

for c in range(1, 7):
    numero_da_vez = int(input('Digite um número inteiro: '))
    if numero_da_vez % 2 == 0:
        variavel_acumuladora += numero_da_vez

print(variavel_acumuladora)