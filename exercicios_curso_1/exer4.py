def qual_o_quadrante(x, y):
    if x > 0 and y > 0:
        return 'Primeiro quadrante'
    elif x < 0 and y > 0:
        return 'Segundo quadrante'
    elif x < 0 and y < 0:
        return 'Terceiro quadrante'
    else:
        return 'Quarto quadrante'

def main():
    x = int(input('Digite um valor para X: '))
    y = int(input('Digite um valor para Y: '))
    resultado = qual_o_quadrante(x, y)
    print(f'Suas coordenadas são: ({x},{y}) e elas estão no {resultado}')

if __name__ == '__main__':
    main()