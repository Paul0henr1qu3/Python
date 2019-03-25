valor_hora = float(input("Valor ganho por hora: "))
horas_trabalhadas = int((input("Horas trabalhadas: ")))

salario_bruto = valor_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato

print "\n"
print "+ Salario Bruto : R$",salario_bruto
print "- IR (11%) : R$", ir
print "- INSS (8%) : R$", inss
print "- Sindicato ( 5%) : R$", sindicato
print "= Salario Liquido : R$", salario_liquido
