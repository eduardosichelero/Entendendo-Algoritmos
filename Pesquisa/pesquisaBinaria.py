def BuscaBinaria(lst, item):
    baixo = 0
    alto = len(lst) - 1

    while baixo <= alto:
        meio = (alto + baixo) // 2
        chute = lst[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


lista_de_numeros = [1, 3, 5, 7, 9]

print(BuscaBinaria(lista_de_numeros, 3))
print(BuscaBinaria(lista_de_numeros, -1))