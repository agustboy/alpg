comida1 = str(input())
comida2 = str(input())

if comida1 == 'Lasanha':
  comida1 = 8
if comida1 == 'Estrogonofe':
  comida1 = 11
if comida2 == 'Refrigerante':
  comida2 = 3
if comida2 == 'Suco':
  comida2 = 2.5
  

soma = comida1 + comida2

print(f"{soma:.2f}")
