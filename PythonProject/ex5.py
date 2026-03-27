nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print("Você foi aprovado")
    print(f"media {media}")
else:
    print("você foi reprovado! ")