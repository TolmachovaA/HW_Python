# Дано двозначне число
number = input("Введіть двозначне число: ")

# Розділимо число на дві цифри
first_digit = int(number[0])
second_digit = int(number[1])

# Визначимо, яка цифра більша
if first_digit > second_digit:
  print("Більша перша цифра:", first_digit)
elif first_digit < second_digit:
  print("Більша друга цифра:", second_digit)
else:
  print("Цифри однакові:", first_digit)