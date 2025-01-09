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
    