import random

numeros_aleatorios = [random.randint(1, 100) for i in range(5)]

print(numeros_aleatorios)

print(f'O menor número é {sorted(numeros_aleatorios)[0]} e o maior número é {sorted(numeros_aleatorios)[-1]}')