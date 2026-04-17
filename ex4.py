quantidade = int(input('informe a quantidade de numero: '))
soma_pares = 0
soma_impares = 0
conta_pares = 0
conta_impares = 0
cont = 0
while cont < quantidade:
    numero = int(input('informe um numero inteiro: '))
    if numero % 2 ==  0:
        soma_pares += numero
        conta_pares += 1
    else:
        soma_impares += numero
        conta_impares += 1
    cont += 1

if conta_pares != 0:
    print(f'Media dos pares: {soma_pares / conta_pares:.2f}')
else:
    print(f'Media dos pares: não há numeros pares')

if conta_impares != 0:
    print(f'Media dos ímpares: {soma_impares / conta_impares:.2f}')
else:
    print(f'Média dos ímpares: não há numeros impares')
