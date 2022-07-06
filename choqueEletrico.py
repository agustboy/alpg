level = int(input())
if 1 <= level <= 20:
  potencia = 20 + level ** 3
elif 21 <= level <= 40:
  potencia = 8000 + (level - 10) ** 2
elif 41 <= level <= 60:
  potencia = 9000 + 5 * level
elif 61 <= level <= 80:
  potencia = 9300 + 2 * level
elif 81 <= level <= 100:
  potencia = 9500 + level
print(f"Potencia de : {potencia} W")
