#Pede ao usuario um numero e faz a tabuada do 1 ao 10
numero = int(input('Digite um número: '))

for i in range(1,10):
    tabuada = numero*i
    print(f'{i} x {numero} = {tabuada}')
