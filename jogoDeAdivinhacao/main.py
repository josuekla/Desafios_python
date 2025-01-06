import random

def exibir_boas_vindas():
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar um número que estou pensando entre 1 e 100.")
    print("Você começa com 1000 pontos e perderá 100 pontos a cada erro.")
    print("Boa sorte!\n")

def obter_palpite():
    while True:
        try:
            palpite = int(input("Digite seu palpite (entre 1 e 100): "))
            if 1 <= palpite <= 100:
                return palpite
            else:
                print("Por favor, insira um número entre 1 e 100.")
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar um número inteiro.")

def jogar():
    numero_secreto = random.randint(1, 100)
    score = 1000
    tentativas = 0
    limite_tentativas = 10

    while tentativas < limite_tentativas:
        palpite = obter_palpite()
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns, você acertou em {tentativas} tentativa(s)!")
            print(f"Seu score final foi: {score}\n")
            return
        elif palpite > numero_secreto:
            print("Seu número foi alto. Tente um número mais baixo.")
        else:
            print("Seu número foi baixo. Tente um número mais alto.")

        score -= 100
        print(f"Score atual: {score}\n")

    print(f"Que pena, você não acertou o número em {limite_tentativas} tentativas.")
    print(f"O número secreto era: {numero_secreto}\n")

def jogar_novamente():
    while True:
        pergunta = input("Deseja jogar novamente? (S/N): ").strip().upper()
        if pergunta in ("S", "N"):
            return pergunta == "S"
        else:
            print("Resposta inválida. Digite novamente.")

def jogo_main():
    exibir_boas_vindas()
    while True:
        jogar()
        if not jogar_novamente():
            print("Obrigado por jogar!")
            break

jogo_main()
