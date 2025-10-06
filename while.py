#Se usa el While para cuando no conocemos el numero de iteraciones y necesitamos realizar algo iterativo, 
#While se traduce como mientras
prom=0
for i in range(3):
    n1=float(input(f'Ingrese nota {i+1}: '))
    while n1>5 or n1<0:
        n1=float(input(f'Ingrese nota {i+1}: '))
    prom=prom+n1
    #prom =+ n1 Variables de acumulacion
prom=round(prom/3,2)
if prom >=3:
    print(f'Aprobado con una nota de {prom}')
else:
    print(f'Reprobado con una nota de {prom}')