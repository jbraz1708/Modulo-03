valores = []
maior = 0
menor = 0
for c in range (0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}:  ')))
    if c == 0: 
        mai = men = valores[c]
    else: 
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor: 
            menor = valores[c]
print(valores)
print(f'O maior número digitado na lista foi: {maior}')
print(f'O menor valor digitado na lista foi: {menor}')