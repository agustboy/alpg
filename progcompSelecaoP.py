sexo = str(input())
tempo = int(input())
salario = float(input())

if sexo == 'h' and tempo > 15:
  bonus = salario + (salario * 0.2)
elif sexo == 'm' and tempo > 10:
  bonus = salario + (salario * 0.25)
else:
  bonus = salario + 200
print(f"{bonus:.2f}")
