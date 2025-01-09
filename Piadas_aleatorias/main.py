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

    