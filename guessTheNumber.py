import random

numero_secreto = random.randint(1, 20)

print("Bem-vindo ao jogo de adivinhação!")
print("Estou pensando em um número entre 1 e 20.")

for tentativas_feitas in range(1, 7):
    palpite = int(input("Qual o seu palpite? "))
    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        break
if palpite == numero_secreto:
    print("Parabéns! Você adivinhou o número em", tentativas_feitas, "tentativas!")
else:
    print("Desculpe, o número secreto era", numero_secreto, ". Tente novamente!")
