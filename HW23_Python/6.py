# Порахувати добуток всіх цілих чисел, від А до B
# Діляться на 2 і діляться на 3 беззалишку

A = int(input("Введіть значення A: "))
B = int(input("Введіть значення B: "))

product = 1

for i in range(A, B + 1):
  if i % 2 == 0 and i % 3 == 0:
    product *= i

print("Добуток:", product)

