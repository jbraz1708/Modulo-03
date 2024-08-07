from datetime import datetime

cadastro = {}

cadastro['nome'] = str(input('Digite seu nome: '))
nascimento = int(input('Ano de nascimento: '))
cadastro['idade'] = datetime.now().year - nascimento
cadastro['ctps'] = int(input('Digite o número do CTPS: '))

if cadastro['ctps'] != 0:
    cadastro['ano de contratação'] = int(input('Digite o ano em que foi contratado na empresa: '))
    cadastro['salário'] = int(input('Digite seu salário: '))
    cadastro['aposentadoria'] = (cadastro['idade'] + (cadastro['ano de contratação'] + 35 - datetime.now().year))
print('-' * 30)

print(cadastro)