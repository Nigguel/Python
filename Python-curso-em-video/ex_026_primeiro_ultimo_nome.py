""" Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente. """

nome = str(input("Digite seu nome completo: ")).strip()
nome_sep = nome.split()
print("Muito prazer em te conhecer!")
print(f"Seu primeiro nome é {nome_sep[0]}")
print(f"Seu último nome é {nome_sep[len(nome_sep)-1]}")