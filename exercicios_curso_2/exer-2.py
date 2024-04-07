#Exercícios
# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro():
    carros =[] # É um atributo da classe, que armazena os carros que serão inseridos posteriormente
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)
    def __str__(self):
        return self.modelo
    
carro_lambo = Carro('Urus', 'vermelho', 2024)

print(carro_lambo)

# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.


# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
class Restaurante():
    restaurantes = []
    def __init__(self, nome, categoria, proprietario, cidade):
        self.nome = nome
        self.categoria = categoria
        self.proprietario = proprietario
        self.cidade = cidade
        self.ativo = False
        Restaurante.restaurantes.append(self)
        # Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante_legal = Restaurante('Restaurante Legal', 'Italiano', 'Renan', 'Venezia')

print(f'{restaurante_legal}')

# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente():
    def __init__(self, nome, cidade, idade, nacionalidade):
        self.nome = nome
        self.cidade = cidade
        self.idade = idade
        self.nacionalidade = nacionalidade
        
    def __str__(self):
        return self.nome
    
cliente_1 = Cliente('José', 'Londrina', 29, 'brasileira')
cliente_2 = Cliente('Maria', 'Curitiba', 23, 'brasileira')
cliente_3 = Cliente('João', 'Belo Horizonte', 35, 'brasileira')

print(f'{cliente_1}, {cliente_2}, {cliente_3}')