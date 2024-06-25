""" Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado. """

dias = int(input("Quantos dias você alugou o carro?: "))
km = float(input("Quantos km você rodou com o carro?: "))
pago_dia = 60 * dias
pago_km = 0.15 * km
print(f"O total a pagar é de R${pago_dia+pago_km:.2f}")