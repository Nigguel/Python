""" Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,27. """

dinheiro = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = 3.27
dolar_compra = dinheiro / dolar
print(f"Com R${dinheiro:.2f} você pode comprar US${dolar_compra:.2f}.")