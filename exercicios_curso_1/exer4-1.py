# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
pessoa = {'nome': 'Renan',
           'idade': 32,
           'cidade': 'Jataizinho',
           'altura': 1.83,
           }

# 2 - Utilizando o dicionário criado no item 1:
# Modificando a idade da pessoa
pessoa['idade'] = 33

# Modificando a cidade da pessoa
pessoa.update({'cidade': 'Ibiporã'})

# Adicionando um campo de profissão
pessoa['profissao'] = 'CEO'

# Removendo o campo "altura"

try:
    #del pessoa['altura'] outra opção seria essa
    pessoa.pop('altura')
except TypeError:
    print('Erro: Não existe essa característica')

# Exibindo os valores atualizados
print('Valores atualizados:')
print(f'Nome: {pessoa['nome']}')
print(f'Idade: {pessoa['idade']}')
print(f'Cidade: {pessoa['cidade']}')
print(f'Profissao: {pessoa['profissao']}')

#3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

quadrados = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25,
}

#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
comida = {'prato': 'espaguete','sobremesa': 'ganache','fruta': 'maça'}

if 'prato' in comida:
    print('\nA chave Prato está na lista!\n')
else:
    print('\na chave Prato está fora da lista!\n')

#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
import string
def contar_frequencia_palavras(frase):
    '''Essa função é responsável por contar a frequencia das palavras escritas na frase da variavel frase'''
    #dividir a frase em palavras
    frase_sem_pontos = frase.lower().translate(str.maketrans('', '', string.punctuation))
    palavras = frase_sem_pontos.split()

    #inicializar um dicionário que armazenará a frequência de cada palavra
    frequencia = {}

    #iterar sobre cada palavra na lista de palavras
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    return frequencia

#Exemplo de uso
frase = 'Eu estou escrevendo esta frase muito legal. Eu escrevi outra frase também.'

resultado = contar_frequencia_palavras(frase)
print('\n', resultado)