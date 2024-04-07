"""Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão.
    Adicione um método especial __str__ para imprimir uma representação em string da pessoa.
    Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano.
    Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada
    com base na profissão da pessoa. """

class Pessoa():
    pessoas =[]

    def __init__(self, nome, idade, profissao):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f'{self._nome} | {self._idade} | {self._profissao}'
    
    def faz_aniversario(self):
        self._idade += 1
        return self._idade
    
    @property
    def saudacao(self):
        if self._profissao:
            return f'Olá, sou {self._nome}! Trabalho como {self._profissao}'
        else:
            return f'Olá, sou {self._nome}!'

pessoa_nova = Pessoa('Renan', 33, '')

print(pessoa_nova)
pessoa_nova.faz_aniversario()
print(f'Nova idade da {pessoa_nova._nome} é {pessoa_nova._idade}')
print(pessoa_nova.saudacao)