x = True
while x == True:
    x = False
    try:
        n = int(input('Digite um número aí bobão: '))
        print(n)
    except ValueError:
        print('Insira um numero pfv')
        x = True