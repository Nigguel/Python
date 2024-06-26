""" Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. """

from math import sin, cos, tan, radians
angulo = float(input("Digite o ângulo que você deseja: "))
rad = radians(angulo)
sen = sin(rad)
cos = cos(rad)
tg = tan(rad)
print(f"O ângulo de {angulo} tem o Seno de {sen:.2f}")
print(f"O ângulo de {angulo} tem o Cosseno de {cos:.2f}")
print(f"O ângulo de {angulo} tem a Tangente de {tg:.2f}")