matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range (0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}] e [{c}] : '))
print(f'{matriz[0]}')
print(f'{matriz[1]}')
print(f'{matriz[2]}')
        