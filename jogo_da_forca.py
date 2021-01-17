import random


def jogar():
    welcome_message()
    palavra_secreta = load_secret_key()

    letras_acertadas = init_correct_letter(palavra_secreta)
    print("Você precisa advinhar a palavra", letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):

        chute = guess_letter()

        if (chute in palavra_secreta):
            verify_guessed_word(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
            if (erros == 4):
                print("Dica: é uma fruta!")

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print("\n", letras_acertadas, "\n")

        if ("_" in letras_acertadas):
            letras_faltando = int(str(letras_acertadas.count('_')))
            print("Ainda faltam acertar {} letras".format(letras_faltando))
        else:
            print("Você acertou a palavra secreta {}!".format(palavra_secreta))

    if (acertou):
        win_message()
    else:
        lose_message(palavra_secreta)


### Funções ###

def welcome_message():
    print("*" * 32)
    print("Bem vindo ao jogo da Forca!")
    print("*" * 32, "\n")


def load_secret_key(nome_arquivo="palavras.txt"):
    palavras = []

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def init_correct_letter(palavra):
    return ["_" for letra in palavra]


def guess_letter():
    chute = input("Me diga, qual letra você acha que compõe essa palavra? ")
    chute = chute.strip().upper()
    return chute


def verify_guessed_word(chute, letras_acertadas, palavra_secreta):
    index = 0

    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def win_message():
    print("      G A N H O U !!    ")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def lose_message(palavra_secreta):
    print("P E R D E U !! Você foi enforcado :( ")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("     Tente de novo!        ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


## FIM DAS FUNÇÕES ##

if (__name__ == "__main__"):
    jogar()
