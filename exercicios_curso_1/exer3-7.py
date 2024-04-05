#7 - Construa um código que calcule a média dos valores em uma lista. 
#Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

def calcula_media(lista_numeros):
    try:
        soma = sum(lista_numeros)
        media = soma / len(lista_numeros)
        return media
    except ZeroDivisionError:
        print('Erro: A lista está vazia')

def main():
    num = [5,5,8,4,5,9]
    resultado = calcula_media(num)
    print(f'A média dos números é é: {resultado}')

if __name__ == '__main__':
    main()
