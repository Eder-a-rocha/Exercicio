valor_hora = float(input('Quanto você ganha por hora: '))
horas_mes = float(input('Número de horas trabalhadas no mês: '))

salario_mes = valor_hora * horas_mes
irrf = salario_mes * 11/100
inss = salario_mes * 8/100
sindicato = salario_mes * 5/100

desconto = irrf + inss + sindicato
salario_liquido = salario_mes - irrf - inss - sindicato

print('*'*30)
print(f'+ Sálario Bruto R$ {salario_mes:.2f}')
print(f'- IR (11%) R${irrf:.2f}')
print(f'- INSS (8%):R${inss:.2f}')
print(f'- Sindicato ( 5%):R${sindicato:.2f}')
print('*'*30)
print(f'Desconto do més R$ {desconto:.2f}')
print('*'*30)
print(f'Salário no liquido mês foi R$ {salario_liquido:.2f}')
