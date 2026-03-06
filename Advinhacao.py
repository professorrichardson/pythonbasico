import random
#Cores no Terminal PY
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO ="\033[33m"
AZUL ="\033[34m"
RESET = "\033[0m"

def escolher_nivel():
    print("\nEscolha o nível: ")
    print("1 -- Fácil (10 tentativas)")
    print("2 -- Médio (5 tentativas)")
    print("3 -- Difícil (3 tentativas)")

    while True:
        nivel_str = input("Digite apenas números (1, 2, 3):  ")
        if not nivel_str.isdigit():
            print(VERMELHO+"Digite apenas números! "+ RESET)
            continue

        nivel = int(nivel_str)

        if nivel == 1:
            return 10
        elif nivel == 2:
            return 5
        elif nivel == 3:
            return 3
        else:
            print(AMARELO+"Escolha apenas 1, 2 ou 3 "+RESET)
        

def jogar():

    print(AZUL+'*****************************'+RESET)
    print(AZUL+'*****Jogo adivinhação********'+RESET)
    print(AZUL+'*****************************'+RESET)

    total_tentativas = escolher_nivel()
    numero_secreto = random.randrange(1,31)
    pontos = 100
    historico = []

    for rodada in range(1, total_tentativas + 1):
        print(f"\nTentativa {rodada} de {total_tentativas}")

        chute_str = input("Digite um número entre 1 e 100:  ")

        if not chute_str.isdigit():
            print(VERMELHO+ "Digite apenas números entre 1 e 100: "+RESET)
            continue

        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print(AMARELO+"Você deve digitar números entre 1 e 100! "+RESET)
            continue
        historico.append(chute)

        if chute == numero_secreto:
            print(VERDE+"\n Você Acertou! "+RESET)
            print(VERDE+ f" Sua pontuação foi: {pontos} pontos"+RESET)
            break
        else:
            pontos -=20
            if chute > numero_secreto:
                print(VERMELHO+"O número secreto é MENOR"+RESET)
            else:
                print(VERMELHO+"O número secreto é MAIOR"+RESET)
    else:
        print(VERMELHO+ f"\n Você perdeu! o número secreto era {numero_secreto}"+RESET)
    print(AZUL+ "\n Histórico de tentativas: "+RESET,historico)
    print(AZUL+ "Fim de JOGO!: "+RESET)


while True: 
    jogar()
    repetir = input("\n Deseja jogar novamente? (s/n)").lower()

    if repetir != "s":
        print(AZUL+"\n Obrigado por jogar"+RESET)
        break

        








   
