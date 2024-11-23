#AND E OR

a=int(input("Diz um número: "))
b= 33
c=40

#uso do AND

#usamos o AND em condicionais quando queremos uma condição MÚLTIPLA em que AMBAS AS CONDIÇÕES QUE CRIAMOS têm de se verificar, ou seja:
if a > b and a>c:
    print("O número que escolheste é maior do que os números em que estou a pensar.")
elif a >b and a<c:
    print("O número que escolheste é maior do que um dos números em que estou a pensar, mas menor do que o outro.")
else:
    print("O número que escolheste é menor do que números em que estou a pensar.")
#uso do OR
#usamos o OR em condicionais quando queremos uma condição MÚLTIPLA em que BASTA QUE UMA DAS CONDIÇÕES se verifique para ser verdadeira, ou seja:
d=int(input("Diz outro número: "))

if d==b or d==c:
    print("Estava a pensar num desses números!")
#aqui, basta que UMA condição se verifique para avançarmos com o código correspondente :)