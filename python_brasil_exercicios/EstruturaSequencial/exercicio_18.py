mb = int(input("Tamanho do arquivo em MB: "))
mbps = float(input("Velocidade de um link de Internet (em Mbps): "))

mbps = mbps / 8

segundos = mb / mbps
minutos = segundos / 60

print "Tempo estimado para download: ", minutos
