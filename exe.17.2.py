instalacao= int(input("""Qual é o teu tipo de instalação? Seleciona um número para prosseguir:

[1] - Residencial:

[2] - Comercial:

[3] - Industrial: """))
consumo= int(input("Quanta energia (em kWh) consome a tua instalação?: "))

pagamento=0

#----------RESOLUÇÃO ALTERNATIVA-------------

if instalacao==1:
    if consumo<=500:
        pagamento = 0.40

        print("Como vives numa instalação RESIDENCIAL [1] e consomes até 500kWh, tens de pagar:", pagamento, "€.")
    elif consumo >500:
        pagamento = 0.65

        print("Como vives numa instalação RESIDENCIAL [1] e consomes mais do que 500kWh, tens de pagar:", pagamento,
              "€.")
elif instalacao==2:
    if consumo <=1000:
        pagamento = 0.55

        print("Como vives numa instalação COMERCIAL [2] e consomes até 1000kWh, tens de pagar:", pagamento, "€.")
    elif consumo>1000:
        pagamento = 0.60

        print("Como vives numa instalação COMERCIAL [2] e consomes mais do que 1000kWh, tens de pagar:", pagamento,
              "€.")

elif instalacao==3:
    if consumo<=5000:
        pagamento = 0.55

        print("Como vives numa instalação INDUSTRIAL [3] e consomes até 5000kWh, tens de pagar:", pagamento, "€.")
    elif consumo>5000:
        pagamento = 0.60

        print("Como vives numa instalação INDUSTRIAL [3] e consomes mais do que 5000kWh, tens de pagar:", pagamento,
              "€.")
else:
    print("Tipo inválido, tenta outra vez.")