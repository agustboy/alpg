idade = int(input())
if 0 <= idade <= 10:
    categoria = 'infantil'
elif 11 <= idade <= 14:
    categoria = 'junior'
elif 15 <= idade <= 20:
    categoria = 'adolescente'
elif 21 <= idade <= 35:
    categoria = 'jovem'
elif idade > 35:
  categoria = 'master'
else: 
  print("Idade invalida")
print(f"{categoria}")
