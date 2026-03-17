x = True
while x == True:
    x = False
    try:
        n = int(input('Digite um número aí bobão: '))
        print(n)
    except ValueError:
        print('Insira um numero pfv')
        x = True

def Fatorial():
    print("------- Fatorial -------------")
    F = int(input("Digite o numero que deseja ver o fatorial: "))
    for i in range(F-1, 0, -1):
        F = F*i
    print(F)

Fatorial()