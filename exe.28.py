numero_inicial=int(input("Escolhe um numero inicial: "))
numero_final=int(input("Escolhe um numero final: "))

par_impar=int(input("Quer números pares[1] ou impares [2]?: "))

soma=0

if par_impar==1:
    print("os numeros pares são: ")

if par_impar==1:
    print("os numeros impares são: ")


for x in range(numero_inicial, numero_final+1):
    if par_impar == 1:
        if x%2== 0:
            print(x, end=" ")
            soma+=x
    elif par_impar==2:
            if x%2 == 1:
                print(x, end=" ")
                soma +=x
    else:
        print("opção invalida!")
        break

if par_impar==1:
    print()
    print(f"A soma de todos os numeros pares é {soma}.")

if par_impar==2:
    print()
    print(f"A soma de todos os numeros impares é {soma}.")