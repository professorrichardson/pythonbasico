saldo = 1000 # global

def sacar():
    global saldo
    saldo = saldo -100
    print("Saldo atual: ", saldo)

sacar()