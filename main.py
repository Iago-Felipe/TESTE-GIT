def Fatorial_rec(n):
    if (n <= 1):
        return 1
    else: 
        return n * Fatorial_rec(n - 1)

def Fatorial(n):
    for i in range(n-1, 0, -1):
        n = n*i
    return n

x = True
while x == True:
    x = False
    try:
        n = int(input('Digite um número aí bobão: '))
        print("")
        print(f"Fatorial iterativo: {Fatorial(n)}")
        print(f"Fatorial recursivo: {Fatorial_rec(n)}")
    except ValueError:
        print('Insira um numero pfv')
        x = True
