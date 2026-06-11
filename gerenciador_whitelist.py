print("Adicionando servidores à Whitelist...")

# Modo 'w' cria o arquivo e escreve as configurações iniciais
with open('whitelist.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write("10.0.0.1\n")
    arquivo.write("10.0.0.2\n")

print("Whitelist criada. Lendo dados do disco:")

# Modo 'r' lê o conteúdo recém-criado
with open('whitelist.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)