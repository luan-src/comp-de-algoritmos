from collections import Counter

def greedy(valor, moedas_disponiveis):
    moedas_utilizadas = []
    moedas_disponiveis.sort(reverse=True)

    for moeda in moedas_disponiveis:
        while valor >= moeda:
            valor -= moeda
            moedas_utilizadas.append(moeda)
    
    return moedas_utilizadas

def imprimir_moedas_utilizadas(moedas):
    contagem = Counter(moedas)
    total = sum(contagem.values())

    for valor in sorted(contagem.keys(), reverse=True):
        qtd = contagem[valor]
        if qtd == 1:
            print(f"{qtd} moeda de {valor} centavo" if valor == 1 else f"{qtd} moeda de {valor} centavos")
        else:
            print(f"{qtd} moedas de {valor} centavos")
    
    print(f"Total de moedas: {total}")

def main():
    valores = [23, 45, 62, 89]
    configuracoes = [
        [1, 2, 5, 10, 25, 50, 100],
        [1, 5, 10, 20, 50, 100],
        [1, 2, 5, 10, 20, 50, 100],
        [1, 5, 12, 24, 50, 100]
    ]
    i = 0

    for valor in valores:
        for configuracao in configuracoes:
            resultado = greedy(valor, configuracao)
            print(f'Greedy [R${valor/100:.2f}, config{i}]')
            imprimir_moedas_utilizadas(resultado)
            print('-------------------------------------------------------------------')
            i += 1
            if i >= 4:
                i = 0

main()

# Teste adicional manual:
print("\nTeste manual: greedy(77, [1, 5, 10, 50])")
resultado = greedy(77, [1, 5, 10, 50])
imprimir_moedas_utilizadas(resultado)




main()
#Para testar o algoritmo com outros valores
#Greedy(centavos, moedas)

print(f'Teste manual para R$0,77 {greedy(77, [1, 5, 10, 50])}')

# configuracoes = [1, 2, 5, 10, 25, 50, 100]
# configuracao_02 = [1, 5, 10, 20, 50, 100]
# configuracao_03 = [1, 2, 5, 10, 20, 50, 100]
# configuracao_04 = [1, 5, 12, 24, 50, 100]