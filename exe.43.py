from datetime import date

hoje=date.today().year

nascimento=int(input("Em que ano nasceste?: "))

idade=hoje-nascimento

if idade < 18:
    print("Ainda não tens idade para entrar no exército. Espera até aos 18 anos.")
else:
    print("Já tens idade suficiente para te alistar.")