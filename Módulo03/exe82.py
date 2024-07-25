lista_full = []
lista_par = []
lista_impar = []
while True:
    n = int(input('Digite um número para ser adicionado a lista: '))
    lista_full.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    r = str(input('Deseja continuar adicionando números a lista? [S/N] '))
    if r in 'Nn':
        break
lista_full.sort()
lista_par.sort()
lista_impar.sort()
print(f'Lista completa de todos os números: {lista_full}')
print(f'Lista dos números pares: {lista_par}')
print(f'Lista dos números impares: {lista_impar}')