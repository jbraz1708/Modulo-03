alunos = {}

alunos['nome'] = str(input('Informe seu nome: '))
alunos['média'] = float(input('Digite sua média: '))

if alunos['média'] <= 5: 
    alunos['situação'] = 'reprovado'
else:
    alunos['situação'] = 'aprovado'

for k,v in alunos.items():
    print(f'{k} é igual a {v}. ')