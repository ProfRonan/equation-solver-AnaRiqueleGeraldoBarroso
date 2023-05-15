import math
num = int(input("Digite um numero: "))
if num < 1 or num > 2:
    print("Grau inválido")
elif num==1:
    print("A equação é do primeiro grau")
    a = int(input("Digite um numero para A: "))
    if a==0:
        print("Valor de a inválido")
    if a!=0:
        b = int(input("Digite um numero para B: "))
        x = (-b/a)
        x = float(x)
        print(f'{x:.2f}')
elif num==2:
    print("A equação é do segundo grau")
    a = int(input("Digite um numero para A: "))
    if a==0:
        print("Valor de a inválido")
    if a!=0:
        b = int(input("Digite um numero para B: "))
        c = int(input("Digite um numero para C: "))
        delta = ((b*b)-4*a*c)
        if delta < 0:
            print("A equação não possui raízes reais")
        if delta==0:
            print("A equação possui uma raiz real")
            r = -b / (2*a)
            print(f'{r:.2f}')
        if delta > 0:
            print("A equação possui duas raízes reais")
            r1 = ((-b+ math.sqrt(delta)) / 2*a)
            r1 = float(r1)
            print(f'{r1:.2f}')
            r2 = ((-b - math.sqrt(delta)) / 2*a)
            r2 = float(r2)
            print(f'{r2:.2f}')