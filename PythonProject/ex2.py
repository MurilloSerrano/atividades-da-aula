nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
faltas = int(input("Digite a quantidade de faltas: "))

media = (nota1 + nota2) / 2

if media >= 6:
    if faltas <= 20:
        print("você foi aprovado")
        print(f"Média: {media}")
    else:
         print("você foi reprovado por faltas")
else:
    print("você foi reprovado")
    print(f"Média: {media}")
