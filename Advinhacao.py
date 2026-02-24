import random
print('*****************************')
print('*****Jogo adivinhação********')
print('*****************************')

numero_secreto = random.randrange(1,31)
total_tentativas = 3


for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada,total_tentativas))

    chute_str = input("Digite o seu número: ")
    print("Seu numero é: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 30):
        print("Você deve digitar um número entre 1 e 30! ")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor =  chute < numero_secreto

    if(acertou):
        print("Você Acertou!! ")
        break
    else:
        if(maior):
            print("O seu chute foi maior que o número secreto")
        elif(menor):
            print("O seu chute foi menor que o número secreto")
   

print("Fim de jogo!")