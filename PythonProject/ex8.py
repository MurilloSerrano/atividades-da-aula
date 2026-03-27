vogais = "A", "E", "I", "O", "U"

letra = input("Digite uma letra: ")

if letra.upper() in vogais:
    print("sua letra é uma vogal")
    print(f"Vogal {vogais}")
else:
    print("sua letra não é vogal")