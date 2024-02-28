def BuscaMenor(arr):
    menor = arr[0] # Armazena o menor valor
    menorIndice = 0 # Armazena o maior valor
    for i in range(1, len(arr)):
        if arr[i] < menor:
            minomenor = arr[i]
            menorIndice = i
    return menorIndice


def classificacaoPorSelecao(arr): # Ordenações em um array.
    novoArr = []
    for i in range(len(arr)):
        menor = BuscaMenor(arr) # Encontra o menor elemento do array e adiciona ao novo array.
        novoArr.append(arr.pop(menor))
    return novoArr


print(classificacaoPorSelecao([5, 3, 6, 2, 10]))