def BuscaMenor(arr):
    menor = arr[0]
    menorIndice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            minomenor = arr[i]
            menorIndice = i
    return menorIndice


def classificacaoPorSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = BuscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr


print(classificacaoPorSelecao([5, 3, 6, 2, 10]))