def IMC ():
    global peso
    peso = int(input("Quanto pesas?: "))

    global altura
    altura = float(input("Quanto medes?: "))

    global imc
    imc = peso / (altura * altura)

    print(f"O teu IMC é {imc}.")
def CATEGORIA():
    if imc < 18.5:
        print("A tua categoria de IMC é ABAIXO DO PESO.")
    elif imc < 24.9:
        print("A tua categoria de IMC é NORMAL.")
    elif imc < 29.9:
        print("A tua categoria de IMC é ACIMA DO PESO.")
    elif imc < 39.9:
        print("A tua categoria de IMC é OBESIDADE GRAU I.")
    else:
        print("A tua categoria de IMC é OBESIDADE GRAU II.")

IMC()
CATEGORIA()