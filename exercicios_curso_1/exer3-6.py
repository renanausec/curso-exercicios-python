#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

lista = [1,2,3,4,5,6,7,8,9,10]
soma = 0

try:
    for i in lista:
        soma += i
    print(f'a soma dos número é {soma}')
except TypeError:
    print('Erro: Algum elemento da lista não é um número')