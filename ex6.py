hora = int(input('digite um numero: '))
minuto = int(input('digite outro numero: '))
if 0 <= hora <= 23 and 0 <= minuto <= 59:
    print("hora valida")
    print(f'Agora são {hora}:{minuto} ')
else:
    print("hora invalida")

