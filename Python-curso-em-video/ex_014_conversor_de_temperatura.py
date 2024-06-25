"""Escreva um programa que converta uma temperatura digitada em °C e converta para °F."""

temperatura = float(input("Informe a temperatura em °C: "))
farenheit = (temperatura * 9/5) + 32
print(f"A temperatura de 31.5°C corresponde a {farenheit:.1f}°F.")
