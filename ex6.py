import math

menor = math.inf
maior = -math.inf

cont =  0
while cont < 10:
    numero = int(input("infome um numero: "))
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero
    cont += 1

print(f"menor numero: {menor}")
print(f"maior numero: {maior}")