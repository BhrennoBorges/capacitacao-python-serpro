def imprimir_tabela(dados_tabela):
    # Cria uma lista de larguras baseada no número de colunas (3)
    colunas_largura = [0] * len(dados_tabela)
    
    # Encontra a maior palavra de cada coluna
    for i in range(len(dados_tabela)):
        for palavra in dados_tabela[i]:
            if len(palavra) > colunas_largura[i]:
                colunas_largura[i] = len(palavra)
                
    # Loop Externo: Controla as linhas (4 itens em cada coluna)
    for linha in range(len(dados_tabela[0])):
        # Loop Interno: Controla as colunas (3 listas)
        for coluna in range(len(dados_tabela)):
            # Acesso invertido para transpor a matriz: [coluna][linha]
            palavra_atual = dados_tabela[coluna][linha]
            largura_coluna = colunas_largura[coluna]
            
            # Imprime alinhado à direita com um espaço extra no final
            print(palavra_atual.rjust(largura_coluna), end=' ')
        
        # Pula de linha ao terminar todas as colunas daquela linha
        print()

dados_tabela = [
    ['maçãs', 'laranjas', 'cerejas', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['gatos', 'cães', 'alce', 'ganso']
]

imprimir_tabela(dados_tabela)table_printer.py
