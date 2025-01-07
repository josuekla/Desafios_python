class main():
    def __init__(self):
        self.boas_vindas()
        self.opções()
        self.usuario()
        
        
        
    
    def boas_vindas(self):
            print(10*'=' +'Bem vindo ao jogo da forca!' + 10*'=')
            print('Escolha uma categoria:')
            print(' 1 - Profissões\n 2 - Empresas\n 3 - Filmes\n 4 - Países\n 5 - Cores')

    def opções(self):
        category = input('Digite o número da categoria: ')
        if category == '1':
            print('Profissões')
            self.show_word(self.palavras('jobs', 0))
        elif category == '2':
            print('Empresas')
            self.show_word(self.palavras('companies', 0))
        elif category == '3':
            print('Filmes')
            self.show_word(self.palavras('movies', 0))
        elif category == '4':
            print('Países')
            self.show_word(self.palavras('countries', 0))
        elif category == '5':
            print('Cores')
            self.show_word(self.palavras('colors', 0))
        else:
            print('Categoria inválida')

    def palavras(self, category, index=None):
        words = {
        'jobs' : ['dentista', 'programador', 'policial'],
        'companies' : ['google', 'amazon', 'tesla', 'microsoft'],
        'movies' : ['titanic', 'avatar', 'star wars', 'harry potter'],
        'countries' : ['brasil', 'canada', 'alemanha', 'australia'],
        'colors' : ['vermelho', 'azul', 'amarelo', 'verde'],
    }
        return words[category][index] if index is not None else words[category]

    def resposta(self):
        pergunta = input('\nDigite uma letra: ').strip().lower()
        return pergunta
    

    def show_word(self, word):
        letras = []
        print('A palavra é: ')
        for letter in word:
            letras.append(letter)
            print('_', end='')
        if self.resposta() in letras:
            print('Letra encontrada')
            letras
        
        
            # for letter in 
            # if self.usuario() in word:
            #     print('Letra encontrada')

    




if __name__ == '__main__':
    main()
