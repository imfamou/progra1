def encontraletra():
    soma=0
    frase=input("Escreve uma frase")
    letra=input("Que letra desajas procurar")

    for x in frase:
        if x == letra:
            soma+=1
    print(f"esta frase tem {soma} letra {letra}")

encontraletra()