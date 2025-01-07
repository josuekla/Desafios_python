class Calculadora():
	def __init__(self):
		self.instrucoes()
		
	def instrucoes(self):
		print("===== CALCULADORA SIMPLES EM PYTHON =====")
		print("Escolha a operação matemática desejada: ")
		print("1. Soma")
		print("2. Subtração")
		print("3. Multiplicação")
		print("4. Divisão\n")
		
		def soma(self, *args):
			print("Digite o numero para somar: ")
			return sum(args)
			
		def subracao(self, *args):
			resultado = args[0]
			for num in args[1:]:
				resultado -= num
			return resultado
			
		def multiplicacao(self, *args):
			resultado = 1
			for num in args:
				resultado *= num
			return  resultado
		
		def divisao(self, *args):
			try:
				resultado = 1
				for num in args[1:]:
					resultado /= num
				return resultado
			except ZeroDivisionError:
				return ("Erro: O numero náo pode ser dovidido por 0")
				
		def calculo(self):
			while True:
				pergunta = input("Digite o número da operacão que você deseja ou digite 'sair' para.encerrar.").strip()
				if pergunta.lower() == "sair":
					print("calculadora finalizada.")

