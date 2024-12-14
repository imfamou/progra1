#em Python, um ciclo é algo que se repete infinitamente até ter ordem de parar ou uma condição não se verificar

# no ciclo WHILE, temos de indicar a condição que permite que o ciclo continue.
#a cada vez que um ciclo reiniciar, dá-se uma ITERAÇÃO (repetição do ciclo)

#a cada ITERAÇÃO, a condição de um ciclo é novamente avaliada. Quando já não se verificar, o ciclo quebra. (no caso do CICLO WHILE)

#vamos criar um exemplo de ciclo WHILE baseado num cronómetro:

cronometro=10

while cronometro >=1: #esta parte do código verifica que o cronómetro se mantém maior ou igual a 1, ou seja, o ciclo só funcionará enquanto cronómetro>=1
    print(cronometro) #aqui, fazemos print do valor da variável cronómetro a cada iteração
    cronometro-=1 #subtraimos 1 valor a cada resultado da iteração anterior

print("O foguetão está a partir...") #esta print é realizada PÓS CICLO, ou seja. quando cronometro DEIXA DE SER >=1, o ciclo WHILE quebra e dá lugar ao resto do código posterior

# no ciclo WHILE TRUE, não precisamos de indicar a condição para que ele continue, porque vai continuar infinitamente até definirmos quando deve parar
#ao contrário do cilco WHILE, o WHILE TRUE não para automaticamente, ou seja, a condição para ele parar tem de ser VERIFICADA ou VERDADEIRA
#no ciclo WHILE isto não acontece, porque a sua condição tem de DEIXAR DE SE VERIFICAR para que ele pare.

cronometro2=20 #definimos um valor para o nosso cronómetro

while True: #inicia-se o ciclo infinito
    print(cronometro2) #fazemos print do valor da variável NOTA: o python lê o código da ESQUERDA PARA A DIREITA e de BAIXO PARA CIMA, portanto, aquilo que escrevermos primeiro vai ser executado primeiro!
    cronometro2-=1 #subtraimos 1 valor a cada iteração
    if cronometro2<=1: #INTRODUZIMOS A CONDIÇÃO QUE VAI QUEBRAR O CICLO!
        print("O foguetão está a partir...") #código a ser executado durante a quebra
        break#ORDEM IMPERATIVA que o ciclo vai PARAR. SE COLOCARMOS CÓDIGO DEPOIS DO BREAK (mais ainda dentro do ciclo) NÃO VAI SER EXECUTADO!

print("olá!") #esta print funciona porque, pela sua INDENTAÇÃO, mesmo que esteja após a ordem BREAK, está FORA DO CICLO.