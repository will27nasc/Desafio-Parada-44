# 5) Faça um programa que gere as tabuadas do 1 até o 10. 

n = 1

print("Tabuaba 1 ao 10")

while n <= 10:

    print()

    for x in range(1, 11):
        print(f"{n} X {x} = {n * x}")
        
    n += 1