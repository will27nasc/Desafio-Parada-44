# 6) Faça um programa em que o usuário digita um número inteiro e o programa exibe todos os números ímpares do 1 até o valor inserido.

n = int(input('Insira um número '))

print(f"Números ímpares de 1 à {n}")

for x in range(1, n + 1):
    if(x % 2 != 0):
        print(x)