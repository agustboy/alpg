import math
seconds = int(input())
hora = math.floor(seconds / 3600)
minuto = math.floor(seconds % 3600) / 60
segundo = math.ceil(minuto / 60)
print(f"{hora:.0f} h {minuto:.0f} m {segundo:.0f} s")
