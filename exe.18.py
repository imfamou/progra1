velocidade=int(input("A que velocidade passaste no radar"))

limite=80

passagemlimite=0

multa=0

if velocidade>limite:
    passagemlimite=velocidade-limite
    multa=passagemlimite*2

    print(f"Esta a ir muito depressa! passaste { passagemlimite} km/h acima do limite de velocidade! Tens de pagar {multa} euros")
else:
    print(f"boa! Estas dentro do nlimite  de {limite} km/h!")