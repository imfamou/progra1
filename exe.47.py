from time import sleep
contador=int(input("Qual o tempo de lançamento? "))
print("O foguete será lançado em")
while (contador>0):
    print(contador)
    contador-=1
    sleep(1)
    if contador==3:
        print("Erro no motor")
        break
print("Lançado ...")