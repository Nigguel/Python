""" Faça um progrma que leia tres números e mostre qual é o maior e qual é o menor. """

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))

if n1 > n2 and n1 > n3:
    print(f"O maior valor é {n1}")
elif n2 > n1 and n2 > n3:
    print(f"O maior valor é {n2}")
else:
    print(f"O maior valor é {n3}")

if n1 < n2 and n1 < n3:
    print(f"O menor valor é {n1}")
elif n2 < n1 and n2 < n3:
    print(f"O menor valor é {n2}")
else:
    print(f"O menor valor é {n3}")