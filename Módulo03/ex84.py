pessoas = list() #lista
dado = list()   #incremento da lista
pesadas = [] # variável para as pessoas mais pesadas
leves = [] # variável para as pessoas mais leves
qnt = 0 # variável para a quantidade de pessoas cadastradas 

#Condição
while True: 
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    r = str(input('Deseja continuar adicionando ? [S/N] '))
    if r in 'Nn':
        break

#Pesos 
for p in pessoas:
    if p[1] >= 100:
        print(f'{p[0]} está acima do peso.')
        pesadas.append(p[0])  
    else:
        print(f'{p[0]} é bem leve.')
        leves.append(p[0])
        
#Pessoas pesadas
print('---- Listagem das Pessoas Pesadas ----')
print(pesadas)
#Pessoas Leves
print('---- Listagem das Pessoas leves ----')
print(leves)
#qnt de pessoas
print(f'A quantidade de pessoas cadastradas foram de: {len(pessoas)}')

print(pessoas)