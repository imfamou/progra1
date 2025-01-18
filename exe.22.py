#------------EX 22----------------
#------------CICLO FOR-----------------

#enquanto que os ciclos WHILE correm infinitamente, o ciclo FOR existe para quando queremos controlar a QUANTIDADE DE ITERAÇÕES (repetições) que faz.
#nos ciclos FOR existe um dado que monitoriza as vezes que eles se repetem chamado VARIÁVEL DE ITERAÇÃO
#depois, basta-nos definir qual é o dado que vai limitar a repetição do ciclo, que pode ser uma variável de qualquer tipo ou uma string
#o ciclo vai-se repetir de acordo com o ÍNDICE dos dados que inserirmos, ou seja, por exemplo, a quantidade de carateres num dado de texto (string), a quantidade de elementos numa lista (ÍNDICE DE CADA ELEMENTO DA LISTA), entre outros
#o ÍNDICE, em python, é a ORDEM em que um elemento está, que começa a contar do ZERO (0)

#----------EXEMPLO + LÓGICA DA ESTRUTURA-----------
# VARIÁVEL DE ITERAÇÃO, ou seja o elemento que vai PERCORRER O SEGUNDO ELEMENTO DO CICLO
#   |    SEGUNDO ELEMENTO DO CICLO, ou seja, o PARÂMETRO que LIMITA A QUANTIDADE DE ITERAÇÕES DO CICLO
#   |       |    a palavra TESTE tem 5 LETRAS. o primeiro carater da palavra tem ÍNDICE 0
#   v       v
for x in "TESTE": #aqui, dá-se a avaliação da condição, ou seja, a variável de iteração x vai percorrer a palavra TESTE
    print(x)
#aqui, por cada ITERAÇÃO, ou seja, CADA VEZ QUE A VARIÁVEL DE ITERAÇÃO PERCORRE UMA LETRA, O CICLO CONTINUA ATÉ AS LETRAS ACABAREM
# contudo, mesmo que o ciclo FOR tenha um número de ITERAÇÕES definido, podemos interrompê-lo a qualquer altura
# para tal, basta indicarmos o comando BREAK!
# de modo a inserir esta instrução, devemos indicar as condições sob as quais o nosso ciclo deve parar!
#por exemplo:
# contudo, mesmo que o ciclo FOR tenha um número de ITERAÇÕES definido, podemos interrompê-lo a qualquer altura
# para tal, basta indicarmos o comando BREAK!
# de modo a inserir esta instrução, devemos indicar as condições sob as quais o nosso ciclo deve parar!
#por exemplo:

for v in "SHARKCODERS": #aqui, a VARIÁVEL DE ITERAÇÃO VAI PERCORRER A PALAVRA
    print(v)
    if v=="O": #inserimos a condição de quebra
        break  #mandamos o ciclo parar, ou seja, interrompemos

#---------FUNÇÃO RANGE()----------------

# o ciclo FOR pode incluir funções que determinam a quantidade de vezes que se vai repetir (QUANTIDADE DE ITERAÇÕES)
#a função range() tem exatamente esse propósito.
#dentro dos parêntesis, podemos incluir apenas um parâmetro/argumeno que, neste caso, seria um número que por sua vez irá controlar as repetições do ciclo
#o que acontece é que a variável de iteração percorrerá essa contagem a partir do 0
# TODAS AS CONTAGENS EM PYTHON COMEÇAM A PARTIR DO ZERO (0)

#a estrutura será a seguinte:

for x in range(6): #aqui, a variável de iteração percorrerá uma contagem de 6 (a começar do 0)
    print(x) #vão ocorrer 6 prints até ao ciclo terminar, ou seja, do 0 ao 5

#também podemos incluir dois argumentos/parâmetros.
#isto implica que determinamos um número inicial para a sequência e um número final, contando desde o primeiro número até ao útlimo que definirmos
#no entanto, a contagem vai ocorrer até ao número anterior ao número do segundo parâmetro

for u in range(2,8): #aqui temos uma contagem do 2 ao 8, ou seja, 6 números entre eles
    print(u) #vão ocorrer 6 iterações, ou seja, do 2 ao 7

#podemos, ainda, adicionar mais um argumento. este argumento indica o valor de INCREMENTO, ou seja, DE QUANTO EM QUANTO ESTAMOS A CONTAR!

for b in range(2,20,2): #aqui, o primeiro argumento é o número de início da contagem, o segundo argumento é até onde vamos contar, e o terceiro argumento é de quanto em quanto vamos contar
    print(b, end="") #aqui, adicionamos a função END para que o resultado apareça na horizontal e não na vertical