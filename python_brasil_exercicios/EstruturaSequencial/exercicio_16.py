metros_quadrados = int(input("Quantos metros quadrados: "))

litros = metros_quadrados / 3

if litros <= 18:
    latas = 1
else:
    latas = round(litros / 18)

valor_total = 80.0 * latas

print "\n"
print "Latas necessarias: ", latas
print "Valor total: ", valor_total
