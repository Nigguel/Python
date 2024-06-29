"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import choice
from time import sleep

print("-=-" * 17)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
numeros = [0, 1, 2, 3, 4, 5]
numero = choice(numeros)
print("-=-" * 17)
escolha = int(input("Em que número eu pensei?: "))
print("Processando...")
sleep(2)
if escolha == numero:
    print(F"Paraben, você acertou! Eu pensei no número {numero}")
else:
    print(F"Você errou! Eu pensei no número {numero}")
