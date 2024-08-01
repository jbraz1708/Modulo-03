matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = [] 
for l in range (0, 3):
    for c in range(0, 3):
        matriz[l][c] = float(input(f'Digite um valor para [{l}] e [{c}] : '))
        if matriz[l][c] % 2 == 0:
            soma_par.append(matriz[l][c])

# exibindo os valores 
print(f'{matriz[0]}')
print(f'{matriz[1]}')
print(f'{matriz[2]}')

#Soma dos valores pares
soma_total = sum(soma_par)
print(soma_total)    

#soma dos valores da 3 coluna
terc_colum = []
terc_colum.append(matriz[0][2])
terc_colum.append(matriz[1][2])
terc_colum.append(matriz[2][2])  
terc_colum_soma = sum(terc_colum)
print({terc_colum_soma})

#O maior valor da segunda linha 
maior = 0
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}')