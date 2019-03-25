peso = float(input("Digite o peso do peixe: "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4

    print "Peso acima do estabelecido pelo regulamento de pesca do estado de Sao Paulo (50 quilos)"
    print "Excesso: ", excesso
    print "Multo pelo excesso: ", multa

else:
    print "Peso: ", peso
    print "Peso dentro do estabelecido pelo regulamento de pesca do estado de Sao Paulo (50 quilos)"
