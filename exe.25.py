numero_inicial = int(input("Digite o numero inicial: "))

numero_final = int(input("Digite o numero final: "))

incremento = int(input("Digite o incremento (passo): "))
print(f"Os numeros entre  {numero_inicial} e {numero_final} incremento {incremento} são:")
for i in range(numero_inicial,numero_final + 1, incremento ):
    print(i)