from datetime import date

hoje=date.today().year

nascimento=int(input("Em que ano nasceste?: "))

idade=hoje-nascimento

if idade <=9:
    print("Estás na categoria Benjamim.")
elif idade <=14:
    print("Estás na categoria Infantil.")
elif idade <=19:
    print("Estás na categoria Júnior.")
elif idade <=25:
    print("Estás na categoria Sénior.")
else:
    print("Estás na categoria Master.")