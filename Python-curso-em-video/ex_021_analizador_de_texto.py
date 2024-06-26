""" Crie um programa que leia o texto e mostre na tela:
- O texto com todas as letras em maiúsculas
- O texto com todas as letras em minúsculas
- Quantas letras tem ao todo
- Quantas letras tem a primeira palavra """

texto = str(input("Digite o que você quiser: "))
print(f"Analizando o texto...")
print(f"O texto em maiúsculas é: {texto.upper()}")
print(f"O texto em minúsculas é:{texto.lower()}")
print(f"O texto tem ao todo {len(texto) - texto.count(' ')} letras")
print(f"A primeria palavra do texto tem {texto.find(' ')} letras")