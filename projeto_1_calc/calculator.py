# -*- coding: utf-8 -*-
"""Calculator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YYj3kXkVPQz-bCLqMV96VFG_IaVmUOHE

Calculadora Inteligente
"""

def calculator(name):
  x = int(input("\nAgora, digite o primeiro valor: "))
  y = int(input("Agora, o segundo valor: "))

  print("\nAbaixo, segue o resultado dos cálculos matemáticos")
  print(f"\n{name}, o resultado da soma entre {x} e {y} é: {x + y}")
  print(f"{name}, o resultado da subtração entre {x} e {y} é: {x - y}")
  print(f"{name}, o resultado da multiplicação entre {x} e {y} é: {x * y}")
  if y != 0:
    print(f"{name}, o resultado da divisão inteira entre {x} e {y} é: {x // y}")
  else:
    print("Não é possível dividir por zero")
  print(f"{name}, o resultado da potenciação entre {x} e {y} é: {pow(x, y)}")

name = input("\nOlá, bem vindo(a) a Calculadora Inteligente! Poderia informar o seu nome? ")

while True:
  calculator(name)
  resp = input("\nDeseja incluir novos valores? Responda digitando S(Sim) ou N(Não)").strip().lower()

  match resp:
   case "s" | "sim":
      continue
   case "n" | "não":
      print(f"\nAté mais, {name}!. Obrigado por usar a nossa calculadora :)")
      break
   case _:
      print("\nResposta inválida, com isto, o programa será encerrado. Caso queira continuar, inicie o programa novamente")
      break