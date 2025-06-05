def radix_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        # Contar ocorrências do dígito atual
        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        # Acumular contagem
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Construir saída ordenada com base no dígito
        for i in reversed(range(n)):
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1

        # Copiar de volta para o array original
        for i in range(n):
            arr[i] = output[i]

        exp *= 10

    return arr # Output: [2, 24, 45, 66, 75, 90, 170, 802]