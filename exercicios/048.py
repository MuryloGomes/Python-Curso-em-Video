variavel_acumuladora = 0

for c in range(1, 501):
    if c % 3 == 0:
        variavel_acumuladora += c

print(f'A soma de todos os números impares multiplos de 3 é {variavel_acumuladora}')