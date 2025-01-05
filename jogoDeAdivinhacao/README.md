# Jogo da Adivinhação

Este é um simples jogo da adivinhação criado em Python. O objetivo é adivinhar um número secreto gerado aleatoriamente dentro de um intervalo determinado.

## Como Funciona
- O programa gera um número aleatório entre um limite inferior e superior (por padrão, entre 1 e 100).
- Você tem até 10 tentativas para adivinhar o número.
- Após cada tentativa, o programa fornece uma dica se o número secreto é maior ou menor que o chute.
- Sua pontuação inicial é 100 e diminui a cada tentativa errada.

## Funcionalidades
- **Intervalo Personalizável:** O número secreto é gerado dentro de um intervalo configurável (padrão: 1-100).
- **Limite de Tentativas:** Número máximo de tentativas configurável (padrão: 10).
- **Pontuação Dinâmica:** A pontuação começa em 100 e diminui 10 pontos por tentativa errada.
- **Feedback Dinâmico:** Indica se o número secreto é maior ou menor após cada palpite.
- **Validação de Entrada:** Trata entradas inválidas (como letras ou números fora do intervalo).

## Pré-requisitos
- Python 3 instalado no seu sistema.

## Como Jogar
1. Clone o repositório ou copie o código do arquivo `jogo_adivinhacao.py`.
2. Execute o programa no terminal:
   ```bash
      python jogo_adivinhacao.py 