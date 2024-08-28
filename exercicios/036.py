valor_da_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
quantos_anos_vai_pagar = int(input('Digite a quantidade de anos que você deseja pagar: '))

valor_da_prestação = valor_da_casa / (quantos_anos_vai_pagar * 12)

if valor_da_prestação > salario/100 * 30:
    print('O seu empréstimo foi negado')