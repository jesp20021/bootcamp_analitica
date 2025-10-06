"""numero = -5
if numero>0:
    print('El numero es positivo')
elif numero == 0:
    print('El numero es cero')
else:
    print('El numero es negativo')

calificacion=12
if calificacion >= 90:
    print('Tu calificacion es A.')
elif calificacion >=80:
    print("Tu calificacion es B.")
elif calificacion>=70:
    print("Tu calificación es C.")
elif calificacion>=60:
    print("Tu calificación es D.")
else:
    print("Tu calificación es F.")"""
nota1=float(input('Ingrese la nota 1: '))
nota2=float(input('Ingrese la nota 2: '))
nota3=float(input('Ingrese la nota 3: '))
prom=round(((nota1+nota2+nota3)/3),2)
if prom>=3.0:
    print('El estudiante paso la materia con un promedio de ', prom)
else:
    print('El estudiante no paso la materia ya que su promedio es de ', prom)
