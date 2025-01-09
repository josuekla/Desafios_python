import requests

def joke_randow():
    url = ' https://us-central1-kivson.cloudfunctions.net/charada-aleatoria'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            joke_data = response.json()
            return joke_data
        else:
            return 'Não foi possível obter a piada'
    except requests.exceptions.RequestException as e:
        print(f'Erro: {e}')
        return None
def display_joke(joke):
    if joke:
        print("\n===== PIADA DO DIA =====")
        print(f"{joke['setup']}")
        input("\nPressione Enter para ver a resposta...")
        print(f"{joke['punchline']}")
        print("=========================")
    else:
        print("Nenhuma piada encontrada.")

def main():
    print("===== CONSULTOR DE PIADAS =====")
    while True:
        print("\nEscolha uma opção:")
        print("1. Mostrar uma piada")
        print("2. Sair")
        escolha = input("\nDigite sua escolha: ").strip()

        if escolha == "1":
            joke = joke_randow()
            display_joke(joke)
        elif escolha == "2":
            print("Saindo... Obrigado por usar o consultor de piadas!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

    