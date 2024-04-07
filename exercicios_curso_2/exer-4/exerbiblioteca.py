# 5 - Crie um arquivo chamado exerbiblioteca.py e importe a classe Livro neste arquivo.
from exer import Livro
# 6 - No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
livro1 = Livro('Aprenda Python', 'Renan Ausec', 2024)
livro2 = Livro('Nutrição para comilões', 'Jorge Matos', 2020)
livro3 = Livro('O caçador de pipas', 'Joseph J.', 2023)
livro4 = Livro('O Louco', 'Leone.', 2023)
livro5 = Livro('O Pingaiada', 'Mark Dward.', 2023)

Livro.emprestar(livro3)
Livro.emprestar(livro1)

# 7 - No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
Livro.verificar_disponibilidade(2023)

#Restante no arquivo main.py