numberb = int(input())
numbers = int(input())

concept = numbers / numberb

if concept <= 8:
  print("A")
if 9 <= concept <= 12:
  print("B")
if 13 <= concept <= 18:
  print("C")
if concept > 18:
  print("D")
