nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print("Parábens!")
    print("você foi aprovado ")
    print(f"Média: {media}")

else:
    print("você foi reprovado")
    print(f"Média: {media}")