class Calculadora():
	def __init__(self):
		instrucoes()
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
			resultado = valores[0]
			for num in valores[1:]:
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

		def pergunta_init(self):
			main = input("Qual operacão matemática deseja?")
		
def instrucoes():
	print("CALCULADORA SIMPLES EM PYTHON")
	print("Faça o seu calculo matemático a seguir \n")
	
def subtracao(*args)

	
	
	
instrucoes()
calculo()
