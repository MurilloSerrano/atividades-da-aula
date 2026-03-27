print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("escolha uma das opções acima: "))

a = float(input("digite um numero: "))
b = float(input("digite outro numero: "))

if opcao == 1:
    print(f"resultado da soma: {a+b}")
elif opcao == 2:
    print(f"Resultado da subtração: {a - b}")
elif opcao == 3:
    print(f"Resultado da multiplicaçaõ: {a * b}")
elif opcao == 4:
    if b != 0:
        print(f"resultado da divisão: {a / b}")
    else:
        print("Ocorreu uma divisão por zero")
else:
    print("A opção escolhida é inválida")
