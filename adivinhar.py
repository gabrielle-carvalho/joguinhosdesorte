import random
sorteio = random.randrange(1, 100)
acerto = False
n = 0
print("Bem-vindo ao jogo.\n")

while acerto == False:
    tentativa = int (input("Digite um número entre 1 e 100 e tente acertar o número secreto: "))
    n+=1
    if tentativa > sorteio:
        print("O número secreto é menor que ", tentativa)
    elif tentativa < sorteio:
        print("O número secreto é maior que ", tentativa)
    else:
        print("PARABÉNS!!! Você acertou o número.\n")
        print("Conseguiu em {} tentativas" . format(n))
        acerto = True
