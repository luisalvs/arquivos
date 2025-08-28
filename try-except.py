

# filename = 'alice.txt'

# try:
#     with open(filename) as file:
#         file.read()
# except FileNotFoundError:
#     print('Esse arquivo não existe nesse diretorio')

while True:
    
    try:
        num1 = int(input('Informe um número: '))
        num2 = int(input('Informe um número: '))

    except ValueError:
        print('Digite um número por favor')

    else:
        print(num1 + num2)

