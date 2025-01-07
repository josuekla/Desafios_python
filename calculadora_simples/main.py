class Calculadora:
    def __init__(self):
        self.instrucoes()
        self.calculo()

    def instrucoes(self):
        print("===== CALCULADORA SIMPLES EM PYTHON =====")
        print("Escolha a operação matemática desejada: ")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão\n")

    def soma(self, *args):
        return sum(args)

    def subtracao(self, *args):
        resultado = args[0]
        for num in args[1:]:
            resultado -= num
        return resultado

    def multiplicacao(self, *args):
        resultado = 1
        for num in args:
            resultado *= num
        return resultado

    def divisao(self, *args):
        try:
            resultado = args[0]
            for num in args[1:]:
                resultado /= num
            return resultado
        except ZeroDivisionError:
            return "Erro: O número não pode ser dividido por 0."

    def calculo(self):
        while True:
            operacao = input("Digite o número da operação que você deseja ou digite 'sair' para encerrar: ").strip()
            if operacao.lower() == "sair":
                print("Calculadora finalizada.")
                break

            numeros = input("Digite os números separados por espaço: ").strip()

            try:
                args = [float(num) for num in numeros.split()]
            except ValueError:
                print("Erro: Digite apenas valores válidos!")
                continue

            if operacao == "1":
                print(f"Resultado da soma: {self.soma(*args)}")
            elif operacao == "2":
                print(f"Resultado da subtração: {self.subtracao(*args)}")
            elif operacao == "3":
                print(f"Resultado da multiplicação: {self.multiplicacao(*args)}")
            elif operacao == "4":
                print(f"Resultado da divisão: {self.divisao(*args)}")
            else:
                print("Operação inválida! Tente novamente.")

Calculadora()
