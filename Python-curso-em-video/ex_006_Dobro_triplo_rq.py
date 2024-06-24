""" Crie um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada. """

numero = float(input("Digite um número: "))
dobro = numero * 2
triplo = numero * 3
rq = numero ** (1/2)
print(f"O dobro de {numero} é {dobro}.")
print(f"O triplo de {numero} é {triplo}.")
print(f"A raiz quadrada de {numero} é {rq:.2f}.")