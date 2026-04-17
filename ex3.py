soma = 0

while True:
    numero = int(input("informe um numero: "))
    if numero ==0:
        break
    soma += numero

print(f'Somatorio dos numeros: {soma}')