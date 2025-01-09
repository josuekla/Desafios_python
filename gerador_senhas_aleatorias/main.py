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