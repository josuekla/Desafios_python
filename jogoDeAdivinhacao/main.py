import random

def jogo_main():
	print("Bem vindo ao jogo de advinhação")
	print("Tente adivinhar um numero que estou pensando de 1 ao 100.")
	print("Você vai comecar com 1000 pontos, a cada erro perderá 100 pontos ")
	tentativas = 0
	score = 1000
	numero_secreto = random.randint(1, 100)
	while True:
		palpite = int(input("Diga o seu palpite: "))
		
		if palpite == numero_secreto:
			print("Parabéns, você acertou!")
			print(f"o seu score foi: {score}")	
		elif palpite > numero_secreto and palpite <= 100:
			print("Seu número foi alto, tente mais um número mais baixo")
			tentativas += 1
			score -= 100
		elif palpite < numero_secreto and palpite > 0:
			print("Seu número foi baixo, tente mais um número mais alto")
			tentativas += 1
			score -= 100
		elif palpite < 100 or palpite > 100:
			print("Ops, o númeto deve ser entre 1 e 100 :)")
			
jogo_main()
		
			
