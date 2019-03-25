notas = [6.5,7.6,8.7,10]

i = 1
media = 0

for nota in notas:
    print("{0} nota: {1}".format(i,nota))
    media += nota
    i += 1

media = media /4
print("\nMedia: {0}".format(media))
