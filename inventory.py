# Define a função que recebe o dicionário do inventário
def exibir_inventario(inventario_parametro):
    print("Inventário:")
    total_itens = 0
    
    # Usa o método .items() para pegar a chave (item) e o valor (quantidade) ao mesmo tempo
    for item, quantidade in inventario_parametro.items():
        print(str(quantidade) + ' ' + item)
        total_itens = total_itens + quantidade
        
    # Printa o número total de itens calculados
    print("Número total de itens: " + str(total_itens))

# CÓDIGO PRINCIPAL (Fora da função, colado na esquerda)
mochila = {'corda': 1, 'tocha': 6, 'moeda de ouro': 42, 'adaga': 1, 'flecha': 12}

# Chama a função passando a mochila de teste
exibir_inventario(mochila)