""" Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. 
"""
preco_produto = float(input("qual é o preço do produto? R$"))
desconto = preco_produto * 0.05
preco_desconto = preco_produto - desconto
print(f"O produto que custava R${preco_produto:.2f}, na promoção com desconto de 5% vai custar R${preco_desconto:.2f}.")