import math 
seconds = int(input())
hora = seconds / 3600
math.modf(hora)
minuto = hora % 60
segundo = minuto % 60

print(f"{hora} h {minuto} m {segundo} s)
