def continuar(resposta):
    if resposta == 1:
        return True
    else :
        return False

def perguntar():
    resposta = int(input("Digite 1 para continuar ou 2 para Sair: "))
    return resposta

continua = True
resposta = perguntar()

while continua:
    if resposta == 1 or resposta == 2:
        continua = continuar(resposta)
    else:
        print("Por favor escolha 1 para continuar ou 2 para Sair")
        resposta = perguntar()

