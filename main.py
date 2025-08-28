
def ler_arquivo(filename):
    with open(filename) as file:
        print(file.read())

try:
    filenames = ['cats.txt', 'dogs.txt']
    for filename in filenames:
        ler_arquivo(filename)
except FileNotFoundError:
    pass

