import os

x = int(input("Digite o valor da largura: "))
y = int(input("Digite o valor da altura: "))
l = 1
i = 1 
while i <= y:
   print('#' * x, end = '')
   print()
   i = i + 1
   while i > 1 and i < y:
      print('#' + ' ' * (x - 2) + '#')
      i = i + 1

os.system("pause")