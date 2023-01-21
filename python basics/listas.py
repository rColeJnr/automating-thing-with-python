frase = ''
def listas(lista):
    for l in lista:
        global frase
        frase += f'{l}, '
    print(frase)
listas(["a", 'b', 'c'])