import time

primeiro_termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))

for c in range(primeiro_termo, 10*razão, razão):
    print(c)
    time.sleep(1)