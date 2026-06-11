log_bruto = "   erro: falha de autenticacao de rede   \n"
log_limpo = log_bruto.strip()
palavras = log_limpo.split(': ')
nivel_alerta = palavras[0].upper()
mensagem = palavras[1].capitalize()
print(f"[{nivel_alerta} -> {mensagem}]")