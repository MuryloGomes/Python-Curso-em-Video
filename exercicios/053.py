frase = str(input('Digite uma palavra: ')).strip().lower()
final = len(frase) // 2
opc = 0

for c in range(final):
    if frase[c] == frase[-(c + 1)]:
        opc += 1

if opc == final:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
