import random

def exibe_msg_inicio():
    print('*************************************')
    print('Olá, bem vindo ao jogo de adivinhação')
    print('*************************************')

#Variaveis
pontos = 1000
tl_tentativas = 0

exibe_msg_inicio()


def jogar():

    numero_al = random.randint(1, 100)

    print(numero_al)
    print('Qual nível você gostaria de jogar?')
    print('(1)Fácil, (2)Médio, (3)Difícil')

    nivel = int(input('Qual a sua escolha: '))

    if(nivel == 1):
        tl_tentativas = 12
    elif(nivel == 2):
        tl_tentativas = 6
    else:
        tl_tentativas = 3

    #Rodadas
    for rodada in range(1, tl_tentativas + 1):
        print('Tentativas {} de {}'.format(rodada, tl_tentativas))
        chute_str = input("Digite um número ente 1 e 100:")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print('Aceitamos paenas números dentre 1 a 100!!!')
            continue

        correto = chute == numero_al
        menor = chute > numero_al
        maior = chute < numero_al

        if(correto):
            print('Parabéns você acertou o número secreto .')
            break
        else:
            if(maior):
                print('O número que você digitou é menor que o número secreto.')
                if(rodada == tl_tentativas):
                    print('O número secreto era {}.'.format(numero_al))
            elif(menor):
                print("O seu chute foi maior do que o número secreto!")



jogar()

#Repetição do game
while(tl_tentativas == 0):

    reload_game = int(input('Para jogar novamente digite [1], ou pra finalizar o jogo digite [2]: '))

    if (reload_game == 1):
        jogar()

    else:
        print('fim de jogo')
        break
