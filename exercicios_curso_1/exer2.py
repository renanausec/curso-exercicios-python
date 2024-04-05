def faixa_etaria(idade):
    if idade <= 12:
        return 'criança'
    elif 13 <= idade <= 18:
        return 'adolescente'
    else:
        return 'adulto'

def main():
    idade = int(input('Digite sua idade: '))
    resultado = faixa_etaria(idade)
    print(f'Você tem {idade} anos e sua faixa etária é {resultado}')

if __name__ == '__main__':
    main()