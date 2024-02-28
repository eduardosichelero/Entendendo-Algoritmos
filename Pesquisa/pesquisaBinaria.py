def BuscaBinaria(lst, item):
    baixo = 0 # Baixo e alto acompanham a parte da lista que esta sendo buscada
    alto = len(lst) - 1

    while baixo <= alto: # Enquanto ainda não consegiu chegar a um único elemento...
        meio = (alto + baixo) // 2 # verifica o elemento central
        chute = lst[meio]
        if chute == item: # Acha o item
            return meio
        if chute > item: # O chute foi muito alto
            alto = meio - 1
        else: # O chute foi muito baixo
            baixo = meio + 1
    return None # o Item não existe


lista_de_numeros = [1, 3, 5, 7, 9]

print(BuscaBinaria(lista_de_numeros, 3))
print(BuscaBinaria(lista_de_numeros, -1))