cont = 0
cont_menores = 0

while cont < 10:
    idade = int(input("informe a idade: "))
    if idade < 18:
        cont_menores += 1
    cont += 1

print(f'Quantidade de pessoas com idade inferios a 18 anos: {cont_menores}')
