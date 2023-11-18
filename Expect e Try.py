try:
  num1 = int(input("Digite um número: "))
  num2 = int(input("Digite outro número: "))
  resultado = num1 / num2
except ZeroDivisionError:
  print("Erro: Divisão por zero não é permitida.")
except ValueError:
  print("Erro: Digite números válidos.")
else:
  print("O resultado é:", resultado)
