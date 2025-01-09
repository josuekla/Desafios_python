import string
import random

def gerador_senha():
    print(10*"==" + "Gerador de Senhas" + 10*"==")

    while True:
        try:
            tamanho = int(input("Digite o tamanho da senha de no mínimo 6 caracteres: "))
            if tamanho >= 6:
                break
            print("A senha deve ser um número maior ou igual a 6.")
        except ValueError:
            print("Digite um número inteiro.")

    words = string.ascii_letters
    number = string.digits
    special = string.punctuation

    incluir_numeros = input("Deseja incluir números na senha? (s/n): ").strip().lower() == 's'
    incluir_especiais = input("Deseja incluir caracteres especiais na senha? (s/n): ").strip().lower() == 's'

    caracteres = words
    if incluir_numeros:
        caracteres += number
    if incluir_especiais:
        caracteres += special

    senha = []
    if incluir_numeros:
        senha.append(random.choice(number))
    if incluir_especiais:
        senha.append(random.choice(special))

    senha += random.choices(caracteres, k=tamanho - len(senha))

