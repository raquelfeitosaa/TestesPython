def selection_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        # Assume que o primeiro elemento não ordenado é o menor
        indice_menor = i
        
        # Percorre o resto da lista para encontrar um menor ainda
        for j in range(i + 1, n):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
                
        # Realiza a troca se encontrar um elemento menor
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
        
    return lista

# Exemplo de uso:
numeros = [64, 25, 12, 22, 11]
print(selection_sort(numeros))  # Saída: [11, 12, 22, 25, 64]