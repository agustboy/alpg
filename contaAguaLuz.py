agua, custo = input().split('')
agua = float(agua)
custo = float(custo)
valor = agua * custo
esgoto = (agua * 0.8) * custo
valorTotal = esgoto + valor
print(f"{valor:.2f}")
print(f"{esgoto:.2f}")
print(f"{valorTotal:.2f}")
