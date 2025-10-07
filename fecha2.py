#programa que me diga cuantos años tengo en la actualidad
import datetime as data
import dateutil.relativedelta as rela
f1=data.date(2024,10,7)
f2=data.date(2025,10,7)

'''diferencia=rela.relativedelta (f2,f1)
print(f'años: {diferencia.years}')
print(f'meses: {diferencia.months}')
print(f'dias: {diferencia.days}')'''

def cumple (f1):
    f2=data.date.today()
    diferencia=rela.relativedelta (f2,f1)
    return cumple

'''print(f'años: {cumple.years}')
print(f'meses: {cumple.months}')
print(f'dias: {cumple.days}')'''
print()