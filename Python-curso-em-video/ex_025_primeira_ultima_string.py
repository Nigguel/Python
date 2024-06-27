""" Desafio 026: Faça um programa que leia uma frase pelo teclado e mostre: 

1. Quantas vezes aparece a letra 'A'
2. Em que posição ela aparece a primeira vez
3. Em que posição ela aparece a última vez"""

frase = str(input("Digite uma frase: ")).strip().upper()
print(f"A letra 'A' aparece {frase.count('A')} vezes na frase.")
print(f"A primeira letra 'A' apareceu na posição {frase.find('A')+1}")
print(f"A última letra 'A' apareceu na posição {frase.rfind('A')+1}")