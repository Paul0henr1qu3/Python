i = 0
lista_master = []
lista_par = []
lista_impar = []

while i < 20:
    numero = int(input("Digite o numero {0}: ".format(i+1)))
    lista_master.append(numero)

    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

    i += 1

print("Lista principal: ", lista_master)
print("Lista PAR: ", lista_par)
print("Lista IMPAR: ", lista_impar)
