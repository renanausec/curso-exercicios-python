from modelos.carro import Carro

carro_audi = Carro('Audi', 'A8', 'branco')
carro_bmw = Carro('BMW', 'M8', 'azul')
carro_mercedes = Carro('Mercedes', 'S500', 'cinza')

def main():
    Carro.exibir_carros()
    print('\n')
    carro_audi.ligar()

if __name__ == '__main__':
    main()