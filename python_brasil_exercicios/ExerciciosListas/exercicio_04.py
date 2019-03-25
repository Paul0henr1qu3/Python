consoantes = ['B', 'C', 'D', 'F', 'G','J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
conta_consoantes = 0

vetor = ['A','U','I','C','D','E','F','K','M','N']

for letra in vetor:
    if letra in consoantes:
        print(letra)
        conta_consoantes += 1

print("\nQuantidade lidas: {0}".format(conta_consoantes))
