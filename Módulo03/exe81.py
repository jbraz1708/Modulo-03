lista = []
while True:
    numero = int(input('Digite um número para adicionar a lista: '))
    lista.append(numero)
    r = str(input('Deseja continuar adicionando números? [S/N]'))
    if r in 'Nn':
        break
if 5 not in lista:
    print('O valor 5 não foi digitado na lista!')
else: 
    print('O valor 5 foi digitado')    

print(f'A quantidade de números digitados foram: {len(lista)}')
lista.sort(reverse=True)
print(f'Mostrando a lista em ordem decrescente: {lista}')
