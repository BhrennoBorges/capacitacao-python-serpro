def validar_senha(senha):
    # Regra 1: Tamanho
    if len(senha) < 8:
        return False
    
    # Variáveis de controle para as regras
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    
    # Loop que analisa caractere por caractere
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
            
    # Se todas as bandeiras forem verdadeiras, a senha é forte
    return tem_maiuscula and tem_minuscula and tem_numero

# Testes
senhas = ['senha123', 'SENHA123', 'Senha', 'Admin@12345']

for s in senhas:
    resultado = "SEGURA" if validar_senha(s) else "VULNERÁVEL"
    print(f"{s.ljust(15)} -> {resultado}")
