salario_fixo = float(input('Digite o salario fixo: '))
vendas = float(input('Digite o valor de vendas: '))

if vendas <= 1500:
    comissao = vendas * 0.03
else:
    comissao = (1500 * 0.03) + ((vendas - 1500) * 0.05)

salario_fixo = salario_fixo + comissao
print(f"Salario total: {salario_fixo:.2f}")