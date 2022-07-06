altura = float(input())
raio = float(input())
pi = 3.14
volume = pi * raio ** 2 * altura
ab = pi * raio ** 2
al = 2 * pi * raio * altura
area = 2 * ab + al
print(f"{volume:.2f}")
print(f"{area:.2f}")
