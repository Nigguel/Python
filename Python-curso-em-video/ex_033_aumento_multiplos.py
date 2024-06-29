""" Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salarios superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input("Qual é o salário do funcionário? R$: "))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

salario_novo = salario + aumento
print(f"-quem ganhava R$ {salario:.2f} passa a ganhar R$ {salario_novo:.2f} agora.")