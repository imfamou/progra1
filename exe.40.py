from random import randint
tentativas=0
while True:
    dado1 = randint(1, 6)
    dado2 = int(input("Escolhe um numero de 1 a 6: "))
    tentativas = 0

    if dado1 == dado2:
        print(f"O DADO1 deu {dado1}, e o DADO2 deu {dado2}.")
        print(f"Boa! Os dados são iguais. Foram precisas {tentativas} tentativas para chegarmos a este resultado.")
        break
    else:
        print(f"O DADO1 deu {dado1}, e o DADO2 deu {dado2}.")
        print("Oops! Os dados não são iguais.")
        tentativas += 1