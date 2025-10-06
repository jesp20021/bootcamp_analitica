#Primera forma de hacer un For en python
"""for i in range(5):#i arranca en 0 con un range de 5 que es el limitante e itera sobre el range
    print(f'Hello, World {i}')
 
#Segunda forma de incremento y diciendole de donde empieza, donde termina y el incremento
for i in range(13,20,2):
    print(f'Hello, World {i}')"""
    
prom=0
for i in range(3):
    n1=float(input(f'Ingrese nota {i+1}: '))
    prom=prom+n1
    #prom =+ n1 Variables de acumulacion
prom=prom/3
if prom >=3:
    print('Aprobado')
else:
    print('Reprobado')