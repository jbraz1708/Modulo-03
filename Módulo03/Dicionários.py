pessoas = {'nome' : 'João', 'sexo': 'Masculino', 'idade': 21 }

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade e é do sexo {pessoas["sexo"]}')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

#adicionando values e keys no dicionário.
pessoas['peso'] = 95.6

# laço para percorrer os dicionários.
for k, v in pessoas.items():
    print(f'{k} = {v}')