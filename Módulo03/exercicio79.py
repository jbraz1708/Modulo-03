lista = []

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado')
    else: 
        print('Valor duplicado, não vou adicionar')       
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
