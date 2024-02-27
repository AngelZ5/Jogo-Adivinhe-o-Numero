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
        vitoria = SuaResposta == Resposta
        if SuaResposta == Resposta:
            print("Você ganhou!, parabéns.")
            chances = 10
            print("Gostaria de ir para a segunda fase? S/N")
            SegundoIniciador = input("").lower()
            if SegundoIniciador == "s":
                print("A segunda fase vai iniciar em...")
                time.sleep(0.7)
                print("3")
                time.sleep(0.7)
                print("2")
                time.sleep(0.7)
                print("1")
                Resposta2 = random.randint(1, 100)
                Chances2 = 10
                print("Adivinhe o número entre 1 e 100")
                while Chances2 > 0:
                    SuaResposta2 = int(input(""))
                    if SuaResposta2 == Resposta2:
                        print("Você ganhou na segunda fase!, parabéns.")
                        print("Gostaria de ir para a terceira fase? S/N")
                        TerceiroIniciador = input("").lower()
                        if TerceiroIniciador == "s":
                            print("A terceira fase vai iniciar em...")
                            time.sleep(0.7)
                            print("3")
                            time.sleep(0.7)
                            print("2")
                            time.sleep(0.7)
                            print("1")
                            Resposta3 = random.randint(1, 200)
                            Chances3 = 10
                            print("Adivinhe o número entre 1 e 200")
                            
                            while Chances3 > 0:
                                SuaResposta3 = int(input(""))
                                if SuaResposta3 == Resposta3:
                                    print("Você ganhou na terceira fase!, parabéns.")
                                    break
                                elif SuaResposta3 < Resposta3:
                                    print("Chute mais alto")
                                elif SuaResposta3 > Resposta3:
                                    print("Chute mais baixo")
                                Chances3 -= 1
                            if Chances3 == 0:
                                print("FIM DE JOGO")
                                break
                    elif SuaResposta2 < Resposta2:
                        print("Chute mais alto")
                    elif SuaResposta2 > Resposta2:
                        print("Chute mais baixo")
                    Chances2 -= 1
                if Chances2 == 0:
                    print("FIM DE JOGO")
                break
            else:
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