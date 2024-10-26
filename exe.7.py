x=int(input("Quanto mede o lado do quadrado?: "))
perimetro=x*4 #o perímetro é a soma do valor de todos os lados, neste caso podemos multiplicar x por 4, porque é um quadrado e todos os seus lados são iguais
area= x**2 # quando queremos fazer uma potência em python, usamos este símbolo [**] seguido do valor da mesma
# ao  quadrado = **2
#ao cubo = **3
#etc

print("A medida do perímetro do quadrado é: ", perimetro,"e a medida da área é: ",area)