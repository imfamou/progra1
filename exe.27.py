numero=int(input("Escolhe um numero: "))

divisoes=0
for x in range(1,numero+1):
    if numero%x== 0:
        divisoes+=1
        print(x, end=" ")
        
if divisoes>2:
    print()
    print(f"O numero {numero} não é numero primo! Foi divisivel {divisoes} vezes!")
else:
    print()
    print(f"O numero {numero} é numero primo! Foi divisivel {divisoes} vezes!")