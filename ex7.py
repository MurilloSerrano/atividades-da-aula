fatorial = 1
numero = int(input("informe um numero: "))
cont = numero

while cont >= 1:
    fatorial *= cont
    cont -= 1

print(f"{numero}! = {fatorial}")    