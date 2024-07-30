valores = [[], []]

for i in range (1, 8):
    n = int(input(f'Digite o {i}° valor:'))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)

print(valores)
valores.sort()

print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores impares digitados foram: {valores[1]}')  