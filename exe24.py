numero_inicial = int(input("Digite o numero inicial: "))

numero_final = int(input("Digite o numero final: "))

print(f"Os numeros entre  {numero_inicial} e {numero_final} sao")
for i in range(numero_inicial,numero_final + 1):
    print(i)