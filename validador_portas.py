import pyinputplus as pyip

print("=== Configuração de Firewall ===")

# Garante que o usuario digite um número inteiro dentro das portas de rede válidas
porta = pyip.inputInt(prompt="Digite a porta a ser bloqueada (1-65535): ", min=1, max=65535)

# Garante a digitação de um formato "sim/não"
confirmacao = pyip.inputYesNo(prompt=f"Tem certeza que deseja bloquear a porta {porta}? (yes/no): ")

if confirmacao == 'yes':
    print(f"🔒 Regra aplicada: Porta {porta} bloqueada com sucesso.")
else:
    print("Operação cancelada.")