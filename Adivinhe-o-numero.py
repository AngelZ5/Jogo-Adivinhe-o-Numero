import time
import random

print("Bem vindo ao jogo adivinhe o número!")
print("Começar?")
print("S/N")

Iniciador = input("").lower()
if Iniciador == "s":
    print("Ok o jogo vai começar em")
    time.sleep(0.7)
    print("3")
    time.sleep(0.7)
    print("2")
    time.sleep(0.7)
    print("1")
    Resposta = random.randint(1, 50) 
    Chances = 10
    print("Adivinhe o número entre 1 e 50")
    print("Você tem 10 chances")
    while Chances > 0:
        SuaResposta = int(input(""))
        if SuaResposta == Resposta:
            print("Você ganhou!, parabéns.")
            break
        elif SuaResposta < Resposta:
            print("Chute mais alto")
            Chances -= 1
        elif SuaResposta > Resposta:
            print("Chute mais baixo")
            Chances -= 1
        if Chances == 0:
            print("FIM DE JOGO")
            break

elif Iniciador == "n":
    print("Fechando jogo")
    time.sleep(1.5)
