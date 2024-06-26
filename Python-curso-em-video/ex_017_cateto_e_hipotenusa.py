""" Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,"""

from math import hypot

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hipo = hypot(co, ca)
print(f"A hipotenusa vai medir {hipo:.2f}")