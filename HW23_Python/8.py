# Чи є в записі числа цифра 2?

N = int(input("Введіть ціле число N (>0): "))

found = False

while N > 0:
  digit = N % 10
  if digit == 2:
    found = True
    break
  N //= 10

print("TRUE" if found else "FALSE")