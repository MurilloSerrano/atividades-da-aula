nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
faltas = int(input("Digite a quantidade de faltas: "))

media = (nota1 + nota2) / 2

if media >= 6 and faltas <= 20:
    print("voce foi aprovado")
    print(f"media {media}")
elif media >= 6 and faltas > 20:
    print("voce foi reprovado")
else:
    print("voce foi reprovado por media")
    print(f"média: {media}")

