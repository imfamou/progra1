idade_veiculo=int(input("Quantos anos tem o teu veículo?: ")) #aqui, respondemos a idade do nosso veículo para que seja tomada em consideração na CONDICIONAL

#neste exercício, queremos saber se o nosso veículo é SEMINOVO ou ANTIGO
# para ser SEMINOVO, tem de ter menos de 10 anos
# para ser ANTIGO, tem de ter mais de 10 anos

if idade_veiculo <= 10:    #aqui, verificamos a idade do carro segundo os limites para cada tipo (seminovo ou antigo); estamos a ver se o carro tem ATÉ 10 anos.
print("O teu carro é seminovo.")
else: # se a idade não for MENOR nem IGUAL, é MAIOR! ou seja, não precisamos de abrir outro if, basta escrever else.
print("O teu carro é antigo.")