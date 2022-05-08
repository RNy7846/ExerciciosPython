import os

x=int(input("Digite um numero inteiro "))

if (x%5)==0:
    if(x%3)==0:
        print("FizzBuzz")
    else:
        print(x)
else:
    print(x)

os.system("pause")
