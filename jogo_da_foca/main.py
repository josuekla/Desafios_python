class main():
    def __init__(self):
        self.categorias = {
            "1": ('Profissões', ['dentista', 'programador', 'policial']),
            "2":( 'Empresas', ['titanic', 'avatar', 'star wars', 'harry potter']),
            "3": ('Filmes', ['titanic', 'avatar', 'star wars', 'harry potter']),
            "4": ('Países', ['brasil', 'canada', 'alemanha', 'australia']),
            "5": ('Cores', ['vermelho', 'azul', 'amarelo', 'verde']),
        }

        self.palavra_atual = ''
        self.palavra_completa = []
        self.letras_adivinhadas = set()
        
        
        
    
    def boas_vindas(self):
            print("===== BEM-VINDO AO JOGO DA FORCA =====")
            print("Escolha uma categoria:")
            for key, (nome, _) in self.categorias.items():
             print(f"{key} - {nome}")
            print("=======================================\n")

    def opções_categorias(self):
        while True:
            category = input('Digite o número da categoria: ').strip()
            if category in self.categorias:
                _, palavras = self.categorias[category]
                return palavras
            print('Categoria inválida. Tente novamente.')

    def inicializar_palavra(self, palavras):
        import random
        self.palavra_atual = random.choice(palavras)
        self.estado_palavra = ["_"] * len(self.palavra_atual)

    def show_words(self):
        print("\nPalavra: " + " ".join(self.estado_palavra))
            
   

    def resposta(self):
        while True:
            pergunta = input('\nDigite uma letra: ').strip().lower()
            if  len(pergunta) == 1 and pergunta.isalpha():
                return pergunta
            print("Digite apenas uma letra.")
        
        
    def atualizar_palavra(self, letra):
        if letra in self.palavra_atual:
             print(f"A letra '{letra}' está na palavra.")
        for indice, word in enumerate(self.palavra_atual):
            if word == letra:
                self.estado_palavra[indice] = letra
            return True
        else:
            print(f"A letra '{letra}' não está na palavra.")
            return False


    

    
        


if __name__ == '__main__':
    jogo = main()
    jogo.jogo_main()
