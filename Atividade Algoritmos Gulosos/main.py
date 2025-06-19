def greedy(valor, moedas_disponiveis):
    moedas_utilizadas = []
    moedas_disponiveis.sort(reverse=True)

    for moeda in moedas_disponiveis:
        while valor >= moeda:
            valor -= moeda
            moedas_utilizadas.append(moeda)
    
    return moedas_utilizadas

def main():
    valores = [23, 45, 62, 89]
    configuracoes = [[1, 2, 5, 10, 25, 50, 100], [1, 5, 10, 20, 50, 100], [1, 2, 5, 10, 20, 50, 100], [1, 5, 12, 24, 50, 100]]
    i = 0

    for valor in valores:
        for configuracao in configuracoes:
            print(f'Greedy [{valor}, configuracao0{i}] = {greedy(valor, configuracao)}')
            print('-------------------------------------------------------------------')
            i+=1
            if (i>=4):
                i=0

main()

#Para testar o algoritmo com outros valores
#Greedy(centavos, moedas)

print(greedy(77, [1, 5, 10, 50]))

# configuracoes = [1, 2, 5, 10, 25, 50, 100]
# configuracao_02 = [1, 5, 10, 20, 50, 100]
# configuracao_03 = [1, 2, 5, 10, 20, 50, 100]
# configuracao_04 = [1, 5, 12, 24, 50, 100]