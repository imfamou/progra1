from random import randint

pc=randint(0,5)

while True:
    adivinha = int(input("Tenta adivinhar o número em que estou a pensar: "))

    if pc == adivinha:
        print("Parabéns! Acertaste no número!")
        break
    else:
        print("Errado, tenta outra vez.")