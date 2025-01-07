def palavras():
    words = {
        'jobs' : ['dentista', 'programador', 'policial'],
        'companies' : ['google', 'amazon', 'tesla', 'microsoft'],
        'movies' : ['titanic', 'avatar', 'star wars', 'harry potter'],
        'countries' : ['brasil', 'canada', 'alemanha', 'australia'],
        'colors' : ['vermelho', 'azul', 'amarelo', 'verde']
    }

def main():
    print('Bem vindo ao jogo da forca!')
    print('Escolha uma categoria:')
    print('1 - Profissões\n 2 - Empresas\n 3 - Filmes\n 4 - Países\n 5 - Cores')
    category = input('Digite o número da categoria: ')
    if category == '1':
        print('Profissões')
    elif category == '2':
        print('Empresas')
    elif category == '3':
        print('Filmes')
    elif category == '4':
        print('Países')
    elif category == '5':
        print('Cores')
    else:
        print('Categoria inválida')
