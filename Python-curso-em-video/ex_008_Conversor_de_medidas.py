"""Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."""

metros = float(input("Digite uma distância em metros: "))
centimetros = metros * 100
milimetros = metros * 1000
print(f"A distância de {metros}m corresponde a {centimetros}cm e {milimetros}mm.")