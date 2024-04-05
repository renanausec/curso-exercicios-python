#alterar valores de um dicionário

Livro = {
    'titulo': 'Vida do Renan',
    'autor': 'Renan',
    'preco': '59.90',
}

print(f'\nO livro custava {Livro['preco']}\n')

Livro.update({'preco':'69.90'})

print(f'Agora o livro custa {Livro['preco']}\n')

Livro['preco'] = 65.00

print(f'Amanhã o livro custará {Livro['preco']}\n')