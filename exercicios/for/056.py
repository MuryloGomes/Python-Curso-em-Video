idades = 0
homem_mais_velho = 0
nome_homem = 'nome'
mulheres_menos_de_vinte = 0

for c in range(1,5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite seu sexo: ')).lower().strip()
    idades += idade
    if sexo == 'masculino' and idade > homem_mais_velho:
        homem_mais_velho += idade
        nome_homem = nome
    if sexo == 'feminino' and idade < 20:
        mulheres_menos_de_vinte += 1 

print(f'A média de idade do grupo é {idades/4}\no homem mais velho é {nome_homem}\ne a quantidade de mulheres que tem menos de 20 anos é {mulheres_menos_de_vinte}')

