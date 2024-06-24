""" Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média."""

nota_01 = float(input("Digite a primeira nota do alunno: "))
nota_02 = float(input("Digite a segunda nota do aluno: "))
media = (nota_01 + nota_02) / 2
print(f"A média entre {nota_01} e {nota_02} é igual a {media:.2f}.")