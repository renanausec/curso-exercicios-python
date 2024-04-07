# 8 - Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py,
# instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.
from exer import Livro
from exerbiblioteca import *

livro7 = Livro('Tio Patinhas', 'Barbie Girl', 2023)
livro8 = Livro('Pegadinha do Malandro', 'Paul Brussel', 2023)

def main():
    print('Lista dos livros da Biblioteca:\n')
    Livro.listar_livros()

if __name__ == '__main__':
    main()