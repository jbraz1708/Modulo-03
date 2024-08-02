estado = dict()
brasil = list()

for c in range (0,3):
    estado['uf'] = str(input('Digite o estado: '))
    estado['sigla'] = str(input('Digite a sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)

for estado in brasil:
    for k, v in estado.items():
        print(f'O campo {k} tem valor {v}.')
    