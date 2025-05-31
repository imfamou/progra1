listasTimeA = []
listasTimeB = []
listaGolsTimeA = []
listaGolsTimeB = []
timeGoleador = ""
golsGoleador =  0

golsPorTime = []
nomeGolsPorTime = []
while True:
    timeA = input("Qual o nome do time A? Ou x para parar")

    if timeA.lower() == "x":
        break

    timeB = input("Qual o nome do time B?")

    golsTimeA = int(input(f"Quantos gols o {timeA} fez?"))
    golsTimeB = int(input(f"Quantos gols o {timeB} fez?"))
    listasTimeA.append(timeA)
    listasTimeB.append(timeB)
    listaGolsTimeA.append(golsTimeA)
    listaGolsTimeB.append(golsTimeB)

    if (timeA in nomeGolsPorTime):
        posicaoTime = nomeGolsPorTime.index(timeA)
        golsPorTime[posicaoTime] += golsTimeA
    else:
        nomeGolsPorTime.append(timeA)
        golsPorTime.append(golsTimeA)
    if (timeB in nomeGolsPorTime):
        posicaoTime = nomeGolsPorTime.index(timeB)
        golsPorTime[posicaoTime] += golsTimeB
    else:
        nomeGolsPorTime.append(timeA)
        golsPorTime.append(golsTimeA)

posicao = 0
while posicao < len(listasTimeA):
    print("--------------------------------")
    print(f"Time {listasTimeA[posicao]} x {listasTimeB[posicao]}: {listaGolsTimeA[posicao]} x {listaGolsTimeB[posicao]}")

    if listaGolsTimeA[posicao] > golsGoleador:
        golsGoleador = listaGolsTimeA[posicao]
        timeGoleador = listasTimeA[posicao]
    if listaGolsTimeB[posicao] > golsGoleador:
        golsGoleador = listaGolsTimeB[posicao]
        timeGoleador = listasTimeB[posicao]
    print("--------------------------------")
    posicao = posicao + 1

posicao2 = 0
maiorGolsTotal = 0
nomeMaiorGolsTotal = ""
while posicao2 < len(nomeGolsPorTime):
    if golsPorTime[posicao2] > maiorGolsTotal:
        maiorGolsTotal = golsPorTime[posicao2]
        nomeMaiorGolsTotal = nomeGolsPorTime[posicao2]
    posicao2 = posicao2 + 1
#print(f"⚽ O time {timeGoleador} fez o maior numero de gols! Foram {golsGoleador}")
print(f"⚽🏆 O maior número de gols no total foi {maiorGolsTotal} por {nomeMaiorGolsTotal}")