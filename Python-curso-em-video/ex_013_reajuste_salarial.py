""" Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. """

salario_funcionario = float(input("Qual é o salario do funcionário? R$"))
ajuste = salario_funcionario * 0.15
salario_novo = salario_funcionario + ajuste
print(f"Um funcionario que ganhava R${salario_funcionario:.2f}, com 15% de aumento, passa a receber R${salario_novo:.2f}")