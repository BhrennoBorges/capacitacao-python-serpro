import time


nome = input("Olá, usuario. Bem-vindo!, informe seu nome para continuar: ")
print("Olá, " + nome + " seja bem-vindo. :D")

idade = input("ok," +nome+ " poderia me informar sua idade?. : ")
print("Ah, " + nome + " então você tem " + idade + " anos. :D")

print("irei calcular o tamanho do seu nome, aguarde um momento...")
print("Carregando", end="", flush=True)
for i in range(5):
    time.sleep(0.8)
    
    print(".", end="", flush=True)
    
tamanho_nome = len(nome)
print("\nO tamanho do seu nome é:", tamanho_nome, "caracteres. :D")

    

