kwh = float(input())
kwh *= 1.5
desconto = kwh - (kwh * 0.15)
print(f"Valor a ser pago: R$ {kwh:.2f} reais")
print(f"Valor a ser pago com desconto: R$ {desconto:.2f} reais")
