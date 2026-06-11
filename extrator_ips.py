import re

relatorio_rede = "Acessos suspeitos identificados vindos de 192.168.0.15 e do IP externo 203.0.113.50 durante a madrugada."

# \d{1,3} significa "de 1 a 3 números"
molde_ip = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

# O método findall() extrai todas as ocorrências que batem com o molde
ips_encontrados = molde_ip.findall(relatorio_rede)

print("Ameaças detectadas nos seguintes IPs:")
for ip in ips_encontrados:
    print(f"- {ip}")