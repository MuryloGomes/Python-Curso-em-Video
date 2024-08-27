numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezenove', 'vinte')

numero_escolhido = int(input('Digite um número entre 0 e 20: '))

while numero_escolhido < 0 or numero_escolhido > 20:
    numero_escolhido = int(input('Tente novamnete. Digite um número entre 0 e 20: '))
        
print(numeros[numero_escolhido])