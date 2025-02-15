numeros_sorteados=[] #definimos a nossa lista, para a qual irão TODOS os números que sortearmos durante o ciclo. A lista ainda está vazia.


def sorteio():
    for x in range(10): #como queremos que sejam sorteados 10 NÚMEROS, automaticamente entendemos que o ciclo a utilizar deverá ser FOR. Além disso, sabemos a QUANTIDADE de números/vezes a correr o ciclo, então usamos a função RANGE(10), que dará 10 ITERAÇÕES, ou seja, 10 números sorteados :)
        numeros_sorteados.append(randint(1,20))
#esta linha de código fará com que, a cada iteração, seja adicionado um número inteiro aleatório entre 1 e 20 à nossa lista. Isto acontece porque usamos o método APPEND(RANDINT(1,20), que adiciona um item à lista sempre que o ciclo for decorre

    print(f"Os números sorteados foram: {numeros_sorteados}")
def soma_pares():
    soma = 0 #armazenamos os valores para somar
    for x in numeros_sorteados: #VERIFICAÇÃO DO CONTEÚDO DA LISTA, PARA SABER SE TEMOS NÚMEROS PARES!
        if x%2==0: #vemos se o número que a variável de iteração encontrar é par
            print(x) #retornamos o valor do número
            soma+=x #adicionamos os números pares!

    print(f"A soma de todos os números pares é {soma}.")

sorteio() #chamamos as duas funções, para que elas nos retornem os resultados na consola
soma_pares()