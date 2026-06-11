import os
import shutil

nome_pasta = "backup_configuracoes"

# Verifica se a pasta já existe. Se não, cria.
if not os.path.exists(nome_pasta):
    os.makedirs(nome_pasta)
    print(f"📁 Pasta '{nome_pasta}' criada.")

# Copia a whitelist do Capítulo 9 para dentro da pasta de backup
try:
    caminho_destino = os.path.join(nome_pasta, 'whitelist_BKP.txt')
    shutil.copy('whitelist.txt', caminho_destino)
    print(f"✅ Arquivo copiado com segurança para: {caminho_destino}")
except FileNotFoundError:
    print("❌ Erro: O arquivo 'whitelist.txt' não foi encontrado. Rode o script do Cap 9 primeiro!")