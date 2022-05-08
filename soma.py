import os

x = int(input("Digite um número inteiro: "))

y = 0

while (x != 0):
    re = x % 10
    x = (x - re)//10
    y = y + re
print(y)

os.system("pause")
