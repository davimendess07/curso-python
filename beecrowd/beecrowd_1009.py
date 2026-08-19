nome_vendedor = input()
salario_fixo = float(input())
vendas_por_mes = float(input())

comissao = vendas_por_mes * (15 / 100)
total = comissao + salario_fixo

print(f'TOTAL = R$ {total:.2f}')