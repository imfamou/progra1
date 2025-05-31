from random import randint

numero_pc= randint(1, 100)

tentativas=0

while True:
    escolha=int(input("Tenta adivinhar o número em que estou a pensar!: "))
    tentativas+=1
    if escolha > numero_pc:
        print(f"O número em que estou a pensar é menor do que {escolha}.")
    elif escolha<numero_pc:
        print(f"O número em que estou a pensar é maior do que {escolha}.")
    else:
        print(f"Acertaste no número! Foram precisas {tentativas} tentativas para conseguires.")
        break