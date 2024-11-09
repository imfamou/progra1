m=int(input("Escolhe um valor em metros: "))
dm= m*10
cm= m*100
mm= m*1000

# neste exercício, o INPUT é calculado em METROS.
#queremos que o programa nos calcule o valor em DECÍMETROS, CENTÍMETROS, MILÍMETROS, DECÂMETROS, HECTÓMETROS e QUILÓMETROS.
#assim, temos de converter o valor do INPUT para cada uma destas unidades.

dam=m/10
hm=m/100
km= m/1000

print("O valor convertido em DM é:",dm,", em CM é:",cm,", em MM é:",mm, ", em DAM é:", dam,", em HM é:",hm,", e em KM é:",km)