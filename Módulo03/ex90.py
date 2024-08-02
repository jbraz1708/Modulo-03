alunos = {}

for c in range(1):
    alunos['nome'] = str(input('Informe seu nome: '))
    alunos['média'] = float(input('Digite sua média: '))
    if alunos['média'] <= 5: 
        print('Reprovado')
    else:
        print('Aprovado')
print(alunos)