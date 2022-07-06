n, e = map(int, input().split())
g = [int(x) for x in input().split()]
possibility = "NAO"
for i in g:
  for j in g:
    if i + j == e and i != j:
      possibility = "SIM"
      break

  if possibility == "SIM":
    break

print(possibility)

