import random

def jogar():

    print("********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("********************************")

    # inicio em 1 e vai até 100, pois ao chegar no 101 ele para
    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 200

    print("Qual nível de dificuldade do seu jogo?")
    print("Digite 1 para Fácil, 2 para Médio ou 3 para Difícil")

    nivel = int(input("Escolha sabiamente sua dificuldade: \n"))


    if(nivel == 1):
        total_tentativas = 10
    elif(nivel == 2):
        total_tentativas = 7
    else:
        total_tentativas = 5


    for rodada in range(1, total_tentativas + 1):
        print(f"Tentativa {rodada} de {total_tentativas}")
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou ", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto


        if(acertou):
            print("Parabéns! Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute) # número absoluto
            pontos = pontos - pontos_perdidos

        if(rodada == total_tentativas):
            print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))


    print("Fim do Jogo!")

# se for true, ou seja foi aberto este arquivo direto, o código sera executado
# se for false, ou seja, foi executado a partir de outro arquivo/importado,
# apenas se for chamado no arquivo que executara

if(__name__ == "__main__"):
    jogar()