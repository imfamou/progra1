import random

# Função para determinar o vencedor
def vencedor(usuario, computador):
    if usuario == computador:
        return "Empate!"
    elif (usuario == "pedra" and computador == "tesoura") or (usuario == "papel" and computador == "pedra") or (usuario == "tesoura" and computador == "papel"):
        return "Você ganhou!"
    else:
        return "O computador ganhou!"

# Opções do jogo
opcoes = ["pedra", "papel", "tesoura"]

# O usuário escolhe sua opção
usuario = input("Escolha: pedra, papel ou tesoura: ").lower()

# Verifica se a escolha do usuário é válida
if usuario not in opcoes:
    print("Opção inválida. Tente novamente.")
else:
    # O computador escolhe aleatoriamente
    computador = random.choice(opcoes)

    # Exibe as escolhas
    print(f"\nVocê escolheu: {usuario}")
    print(f"O computador escolheu: {computador}")

    # Chama a função para determinar o vencedor
    resultado = vencedor(usuario, computador)

    # Exibe o resultado
    print(resultado)