class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
# 1 - Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
restaurante_praca.categoria = 'Italiana'
print(f'1 - {restaurante_praca.categoria}')
# 2 - Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
print(f'2 - O nome do restaurante é {restaurante_praca.nome}')

# 3 - Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
ativo = 'inativo' if restaurante_praca.ativo == False else 'ativo'
print(f'3 - O restaurante está {ativo}')

# 4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
categoria = restaurante_praca.categoria
print('4 -', categoria)

# 5 - Altere o valor do atributo nome para 'Bistrô'.
categoria = 'Bistrô'
print('5 -', categoria)

# 6 - Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

print(f'6 - O restaurante criado foi: {restaurante_pizza.nome} na categoria {restaurante_pizza.categoria}')

# 7 - Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
categoria = 'A categoria da instância restaurante_pizza é Fast Food' if restaurante_pizza.categoria == 'Fast Food' else 'A categoria não é Fast Food'
print(f'7 - {categoria}')

# 8 - Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True
print(f'8 - O estado da instância restaurante_pizza foi alterado para {restaurante_pizza.ativo} ')

# 9 - Imprima no console o nome e a categoria da instância restaurante_praca.
print(f'9 - Nome: {restaurante_pizza.nome} e Categoria: {restaurante_pizza.categoria}')