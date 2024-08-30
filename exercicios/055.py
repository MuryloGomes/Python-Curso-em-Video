pesos = []

for c in range(1, 6):
    peso = float(input('Digite seu peso: '))
    pesos.append(peso)
    pesos.sort()

print(f'O menor peso é {pesos[0]}, e o maior peso {pesos[5]}')    