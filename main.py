from resources import cafes, recursos, recurso_usuario

class Cafe:
    def __init__(self, tipo, agua, leite, cafe, preco):
        self.tipo = tipo
        self.agua = agua
        self.leite = leite
        self.cafe = cafe
        self.preco = preco

    # Método que trata a forma que o objeto é printado, ao invés de imprimir o endereço de memória
    # .Title() é uma função de formatação de string
    def __str__(self):
        return f"{self.tipo.title()} - Água: {self.agua}, Leite: {self.leite}, Café: {self.cafe}, Preço: R${self.preco:.2f}"

class Recurso:
    def __init__(self, agua, leite, cafe, fichas, dinheiro):
        self.agua = agua
        self.leite = leite
        self.cafe = cafe
        self.fichas = fichas
        self.dinheiro = dinheiro

    def __str__(self):
        return   f'''A maquina possui:
-    {self.agua} mL de água
-    {self.leite} mL de Leite
-    {self.cafe} mg de Café
-    {self.fichas} Fichas 
-    R$ {self.dinheiro:.2f}'''

class RecursoUsuario:
    def __init__(self, fichas, dinheiro):
        self.fichas = fichas
        self.dinheiro = dinheiro

def tipos_de_cafe(cafes):
    lista_cafes = []

    for tipo, dados in cafes.items():
        novo_cafe = Cafe(tipo, **dados)
        lista_cafes.append(novo_cafe)

    return lista_cafes

def exibir_cafes(lista_cafes):
    i = 1
    for cafe in lista_cafes:
        print(f'{i} - {cafe.tipo.title()}')
        i += 1

def cafe_escolhido(lista_cafes, cafe_desejado, recurso):
    match cafe_desejado:
        case 1:
            print('Você escolheu espresso')
            index = 0
            cafe = lista_cafes[index]
            print(cafe)
            qtde_agua = cafe.agua
            qtde_leite = cafe.leite
            qtdo_cafe = cafe.cafe

        case 2:
            print('Você escolheu latte')
            index = 1
            cafe = lista_cafes[index]
            print(cafe)
            qtde_agua = cafe.agua
            qtde_leite = cafe.leite
            qtdo_cafe = cafe.cafe

        case 3:
            print('Você escolheu cappuccino')
            index = 2
            cafe = lista_cafes[index]
            print(cafe)
            qtde_agua = cafe.agua
            qtde_leite = cafe.leite
            qtdo_cafe = cafe.cafe

        case _:
            print('Opção inválida')

    return verificar_recursos(qtde_agua, qtde_leite, qtdo_cafe, recurso)

def iniciar(lista_cafes):
    opcao_valida = True
    print("Iniciando Máquina de Café")
    print("Os tipos de cafés disponíveis na máquina são:")
    exibir_cafes(lista_cafes)
    while opcao_valida:
        cafe_desejado = int(input("Por favor, entre com o nº do tipo de cafe desejado: "))
        if cafe_desejado not in [1, 2, 3]:
            print("Por favor, selecione uma opção válida!")
        else:
            opcao_valida = False
    return cafe_desejado

def recursos_da_maquina():
    recurso_maquina = Recurso(recursos['agua'], recursos['leite'], recursos['cafe'], recursos['fichas'], recursos['dinheiro'])
    return recurso_maquina

def recurso_do_usuario():
    recursos_usuario = RecursoUsuario(recurso_usuario['fichas'], recurso_usuario['dinheiro'])
    return recursos_usuario

def verificar_recursos(qtde_agua, qtde_leite, qtdo_cafe, recurso):
    if qtde_agua > recurso.agua:
        print(f'Quantidade de água ({recurso.agua} mL) insuficiente para café escolhido')
        return False
    elif qtde_leite > recurso.leite:
        print(f'Quantidade de leite ({recurso.leite} mL) insuficiente para café escolhido')
        return False
    elif qtdo_cafe > recurso.cafe:
        print(f'Quantidade de cafe ({recurso.cafe} mL) insuficiente para café escolhido')
        return False
    else:
        return True

def processar_pagamento(recursos_usuario, preco):
    fichas_usuario = recursos_usuario.fichas
    dinheiro_usuario = recursos_usuario.dinheiro

    print("Entre com a quantidade de fichas de cada valor!")
    for i in fichas_usuario.keys():
        fichas_usuario[i] = int(input(f'Entre com a quantidade de fichas de R$ {i}: '))

    for valor_ficha, quantidade in fichas_usuario.items():
        dinheiro_usuario = dinheiro_usuario + (valor_ficha * quantidade)

    if preco == dinheiro_usuario:
        print("Dinheiro suficiente!")
        print("Processando café...")
        print('Café pronto, retire no local indicado!')
        return True, fichas_usuario, dinheiro_usuario

    elif preco < dinheiro_usuario:
        troco = dinheiro_usuario - preco
        print(f'Seu troco é de R$ {troco:.2f}')
        print("Processando café...")
        print('Café pronto, retire no local indicado!')
        return True, fichas_usuario, dinheiro_usuario

    else:
        print("Dinheiro insuficiente!")
        return False, fichas_usuario, dinheiro_usuario

def preco_cafe(cafe_desejado, lista_cafes):
    preco = lista_cafes[cafe_desejado - 1].preco
    return preco

def atualizar_recursos(fichas_usuario, recurso):
    fichas_maquina = recurso.fichas
    for i in fichas_maquina.keys():
        fichas_maquina[i] = fichas_usuario[i]
        fichas_usuario[i] = 0

def continuar(resposta):
    if resposta == 1:
        return True
    else :
        return False

def perguntar():
    resposta = int(input("Digite 1 para continuar ou 2 para Sair: "))
    return resposta




lista_cafes = tipos_de_cafe(cafes)
cafe_desejado = iniciar(lista_cafes)
recurso = recursos_da_maquina()
recursos_usuario = recurso_do_usuario()
print(cafe_escolhido(lista_cafes, cafe_desejado, recurso))

if cafe_escolhido(lista_cafes, cafe_desejado, recurso):
    preco = preco_cafe(cafe_desejado, lista_cafes)
    pagamento_ok, fichas_usuario, dinheiro_usuario = processar_pagamento(recursos_usuario, preco)
    if pagamento_ok:
        atualizar_recursos(fichas_usuario, recurso)

continua = True
resposta = perguntar()
continua = continuar(resposta)

while continua:
    if resposta == 1:
        lista_cafes = tipos_de_cafe(cafes)
        cafe_desejado = iniciar(lista_cafes)
        #recurso = recursos_da_maquina()
        #recursos_usuario = recurso_do_usuario()
        print(cafe_escolhido(lista_cafes, cafe_desejado, recurso))

        if cafe_escolhido(lista_cafes, cafe_desejado, recurso):
            preco = preco_cafe(cafe_desejado, lista_cafes)
            pagamento_ok, fichas_usuario, dinheiro_usuario = processar_pagamento(recursos_usuario, preco)
            if pagamento_ok:
                atualizar_recursos(fichas_usuario, recurso)

        resposta = perguntar()
    else:
        print("Por favor escolha 1 para continuar ou 2 para Sair")
        resposta = perguntar()


    continua = continuar(resposta)

print("Desligando a máquina...")