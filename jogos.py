import jogo_da_forca
import jogo_advinhacao

print("********************************")
print("Bem vindo! Escolha seu jogo!")
print("********************************")


print("Digite 1 para Jogo da Forca e 2 para Jogo de Advinhação!")

jogo = int(input("E ai, qual jogo vai ser? "))

if(jogo == 1):
    print("Você escolheu 1 - Jogo da Forca!")
    jogo_da_forca.jogar()
elif(jogo == 2):
    print("Você escolheu 2 - Jogo de Advinhação!")
    jogo_advinhacao.jogar()

print("Te vejo na próxima!")