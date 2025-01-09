import string
import random

def gerador_senhas_aleatorias(tamanho=8, caracteres=string.ascii_letters + string.digits):
    return ''.join(random.choices(caracteres, k=tamanho))

if __name__ == '__main__':
    gerador_senhas_aleatorias()