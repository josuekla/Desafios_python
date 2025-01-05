import random

def jogo_main():
	print("Bem vindo ao jogo de advinhação")
	print("Tente adivinhar um numero que estou pensando de 1 ao 100.")
	tentativas = 0
	score = 100
	numero_secreto = random.randint(1, 10)
	while True:
		palpite = int(input("Diga o seu palpite"))
		if palpite == numero_secreto:
			print("Parabéns, você acertou!")
			print(f"o seu score foi: {score}")
			
		elif palpite > numero_secreto:
			print("Seu número foi alto, tente mais um número mais baixo")
			tentativas += 1
			score -= 20
		elif palpite < numero_secreto:
			print("Seu número foi baixo, tente mais um número mais alto")
			tentativas += 1
			score -= 20
		else:
			print("Ops, o númeto deve ser entre 1 e 100 :)")
			
jogo_main()
		
			
