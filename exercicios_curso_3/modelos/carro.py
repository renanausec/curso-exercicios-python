from modelos.veiculo import Veiculo

class Carro(Veiculo):
    carros = []

    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self._cor = cor
        Carro.carros.append(self)

    def __str__(self):
        return f'Marca: {self._marca.ljust(15)} | Modelo: {self._modelo.ljust(15)} | Cor: {self._cor}'
    
    def ligar(self):
        print(f' O carro {self._marca} {self._modelo} está ligado')    

    @classmethod
    def exibir_carros(cls):
        if not cls.carros:
            print('Nenhum carro registrado.')
            return
        print('Veículos disponíveis')
        print(f'ID | {"Marca":^15} | {"Modelo":^15} | {"Cor":^15}')
        for i, carro in enumerate(cls.carros, start=1):
            print(f'{str(i).ljust(2)} | {carro._marca.ljust(15)} | {carro._modelo.ljust(15)} | {carro._cor}')
        