def collatz_(number):
    if number % 2 == 0:
        resultado = number // 2
    else:
        resultado = 3 * number + 1
        
    print(resultado)
    return resultado
try:
    numero = int(input("Digite um número inteiro positivo: "))
except ValueError:
    print("Por favor, digite um número inteiro válido.")

while numero != 1:
    numero = collatz_(numero)
    