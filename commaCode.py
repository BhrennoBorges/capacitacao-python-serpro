# Define a função que vai receber uma lista como parâmetro
def formatar_lista(lista_parametro):
    
    # Se a lista estiver vazia (tamanho igual a 0), retorna um texto vazio
    if len(lista_parametro) == 0:
        return ''
        
    # Se a lista tiver apenas 1 item, retorna esse item direto, sem vírgulas
    elif len(lista_parametro) == 1:
        return lista_parametro[0]
   
    # Cria uma string vazia para acumular o texto final do loop
    resultado_string = ''

    # Inicia um loop que vai percorrer cada posição (índice) da lista
    for i in range(len(lista_parametro)):
        
        # REGRA 1: Se for o ÚLTIMO item da lista, adiciona a palavra 'e ' antes dele
        if i == len(lista_parametro) - 1:
            resultado_string = resultado_string + 'e ' + str(lista_parametro[i])
            
        # REGRA 2: Se for o PENÚLTIMO item, adiciona o nome e um espaço (preparando para o 'e')
        elif i == len(lista_parametro) - 2:
            resultado_string = resultado_string + str(lista_parametro[i]) + ' '
            
        # REGRA 3: Para os outros itens normais do início, adiciona uma vírgula e um espaço
        else:
            resultado_string = resultado_string + str(lista_parametro[i]) + ', '
            
    # Devolve a string totalmente montada e formatada para quem chamou a função
    return resultado_string

# CÓDIGO PRINCIPAL (Fora da função)

# Cria uma lista de teste com três itens
lista = ['maçã', 'banana', 'laranja']

# Chama a função passando a nossa lista e mostra o resultado final no terminal
print(formatar_lista(lista))