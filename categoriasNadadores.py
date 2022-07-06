idade = int(input())
if 5 <= idade <= 7:
    categoria = 'Infantil A'
elif 8 <= idade <= 10:
    categoria = 'Infantil B'
elif 11 <= idade <= 13:
    categoria = 'Juvenil A'
elif 14 <= idade <= 17:
    categoria = 'Juvenil B'
elif 18 <= idade <= 40:
    categoria = 'Adulto'
elif idade > 40:
  categoria = 'Master'
else: 
  print("Idade invalida")
print(f"{categoria}")
