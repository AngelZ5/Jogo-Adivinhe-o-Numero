import time
import random

#Apresenta o jogo
print("Bem vindo ao jogo adivinhe o número!")
print("Começar?")
print("S/N")

#Aqui o jogador escolhe iniciar o jogo ou não
Iniciador = input("").lower()
if Iniciador == "s":
    print("Ok o jogo vai começar em")
    time.sleep(0.7)
    print("3")
    time.sleep(0.7)
    print("2")
    time.sleep(0.7)
    print("1")
    #Aqui o numero que deve ser encontrado pra vencer é definido
    Resposta = random.randint(1, 50) 
    #Aqui o jogador recebe 10 chances, A cada final de partida o valor de 10 chances retorna pra conta 
    Chances = 10
    print("Adivinhe o número entre 1 e 50")
    print("Você tem 10 chances")
    #Aqui um loop para que o jogador possa repetir sua jogada a cada chance é criado
    while Chances > 0:
        SuaResposta = int(input(""))
        #Se a sua resposta for igual  a resposta pra vencer o jogo então uma mensagem de Vitoria é emitida (esse comentario vale para todos os mesmos comandos assim)
        if SuaResposta == Resposta:
            print("Você ganhou!, parabéns.")
            print("Gostaria de ir para a segunda fase? S/N")
            #Aqui o jogador escolhe iniciar a segunda fase ou não
            SegundoIniciador = input("").lower()
            if SegundoIniciador == "s":
                print("A segunda fase vai iniciar em...")
                time.sleep(0.7)
                print("3")
                time.sleep(0.7)
                print("2")
                time.sleep(0.7)
                print("1")
                #Dessa vez o numero a ser encontrado alterna de valor e agora é 1 a 100
                Resposta2 = random.randint(1, 100)
                #As 10 chances são restauradas em uma outra variavel chamada Chances2
                Chances2 = 10
                print("Adivinhe o número entre 1 e 100")
                #Mesmo loop para que o jogador possa repetir sua jogada
                while Chances2 > 0:
                    SuaResposta2 = int(input(""))
                    if SuaResposta2 == Resposta2:
                        print("Você ganhou na segunda fase!, parabéns.")
                        print("Gostaria de ir para a terceira fase? S/N")
                        #Aqui a terceira fase acontece, O jogador escolhe ir pra ela ou não assim como as outras
                        TerceiroIniciador = input("").lower()
                        if TerceiroIniciador == "s":
                            print("A terceira fase vai iniciar em...")
                            time.sleep(0.7)
                            print("3")
                            time.sleep(0.7)
                            print("2")
                            time.sleep(0.7)
                            print("1")
                            #Agora o numero de resposta é entre 1 e 200
                            Resposta3 = random.randint(1, 200)
                            #Uma nova variavel de chances é definida com o valor de 10 também
                            Chances3 = 10
                            print("Adivinhe o número entre 1 e 200")
                            #Mesmo loop porem com a nova variavel para o jogador poder tentar novamente
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
        #Se a sua resposta for menor que a resposta pra vencer o jogo então uma mensagem de chute mais alto é emitida (esse comentario vale para todos os mesmos comandos assim)
        elif SuaResposta < Resposta:
            print("Chute mais alto")
            Chances -= 1
            #Se a sua resposta for maior que a resposta pra vencer o jogo então uma mensagem de chute mais baixo é emitida (esse comentario vale para todos os mesmos comandos assim)
        elif SuaResposta > Resposta:
            print("Chute mais baixo")
            Chances -= 1
        if Chances == 0:
            print("FIM DE JOGO")
            break

elif Iniciador == "n":
    print("Fechando jogo")
    time.sleep(1.5)

    