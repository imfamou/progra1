#Solicitando ao usoario que insira um numero

numero = int(input("Digite um numero: "))

#exibindo todos os numeros que antecedem o numero fornecido

print(f"os numeros que antecedem {numero} sao:")
for i in range(numero):
    print(i)