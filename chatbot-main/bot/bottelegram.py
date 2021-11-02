import telebot
from threading import Thread

global TELEGRAM
global CLIENTE
global PRIMEIRA_MENSAGEM


TELEGRAM = "2090274218:AAE8Sn_KcbOGbpHvwZI7HqmWUuTwiL_6QHI"
bot = telebot.TeleBot(TELEGRAM)
valor_cliente = 0
pedido = []


@bot.message_handler(commands=["menu"])
def menu_principal(mensagem):
    texto = """
    Opções: \n /1 acompanhar pedido \n /2 Cancelar o pedido \n /3 Fazer pedido"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["1"])
def acompanhar_pedido(mensagem):
    # colocar status que aparecer no banco usando uma variavel
    texto = """
    Seu pedido está sendo preparado pela equipe e em breve
     estará a caminho"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["2"])
def cancelar_pedido(mensagem):
    # trazer consulta do banco de dado com as informações da mensagem
    itens_pedido = "xxxxxxxxx"
    texto = f"""
    Que pena! \n poderia confirmar o pedido de {itens_pedido}
    /confere ou /naoconfere"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["confere"])
def confere_pedido_cancelado(mensagem):
    # apagar dados do banco
    texto = """
    ok pedido cancelado!
    clique em /menu ou /sair para sair do chat"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["naoconfere"])
def naoconfere_pedido_canceldo(mensagem):
    status = True
    #consulta banco de dado
    if status:
        # se encontrar ele confere e sai do chat
        cancelar_pedido(mensagem)
    else:
        texto = "não foi encontrado nenhum pedido clique em /sair para encerrar o chat."
        bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["3"])
def fazer_pedido(mensagem):
    texto = """*****MENU DE PRODUTO*****\n
    /1B BOLO DE CHOCOLATE R$10,00
    /2B BOLO DE LARANJA R$10,00
    /3B BOLO DE AMENDOIM R$10,00
    /4B BOLO FORMIGUEIRO R$13,00
    /5B BOLO DE LIMÃO R$12,00
    /6B BOLO DE FUBÁ R$17,00
    /7B BOLO DE FUBÁ CREMOSO R$20,00
    /8B BOLO DE FUBÁ COM GOIABADA R$20,00
    /9B BOLO MESCLADO R$22,00
    /10B BOLO DE PRESTIGIO R$22,00
    /11B BOLO DE LEITE NINHO R$35,00
    /12B BOLO DE BRIGADEIRO R$38,00
    /13B BOLO DE NOZES R$40,00
    /14T TORTA DE PRESUNTO E QUEIJO R$20,00
    /15T TORTA DE PALMITO R$20,00
    /16T TORTA DE CARNE MOÍDA R$20,00
    /17T TORTA DE FRANGO R$20,00
    /18T TORTA DE FRANGO COM REQUEIJÃO R$23,00
    /19T TORTA DE FRANGO COM CATUPIRY R$23,00
    /20T TORTA DE ATUM R$25,00
    /21T TORTA NINHO COM OREO R$30,00
    /22T TORTA DE NINHO COM MORANGO R$30,00
    /23T TORTA DE LIMÃO R$30,00
    /24T TORTA DE MARACUJÁ R$30,00
    /25T TORTA DE MORANGO R$3O,00
    /26C CUPCAKE DE CHOCOLATE R$10,00
    /27C CUPCAKE DE VANILHA R$10,00
    /28C CUPCAKE DE MARACUJÁ R$10,00
    /29C CUPCAKE DE CHOCOLATE BRANCO R$10,00
    /30C CUPCAKE DE MORANGO R$10,00
    /31C CUPCAKE DE BRIGADEIRO R$13,00
    /32C CUPCAKE DE DOCE DE LEITE R$13,00
    /33C CUPCAKE DE FRUTAS VERMELHAS R$13,00
    /34C CUPCAKE DE PRESTÍGIO R$13,00
    /35C CUPCAKE DE OVOMALTINE R$16,00
    /36C CUPCAKE DE REDVELVET R$16,00
    /37C CUPCAKE DE NUTELLA R$18,00
    /38C CUPCAKE DE CHOCOLATE BELGA R$18,00"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["1B"])
def bolo_chocolate(mensagem):
    soma_conta_cliente(10, 1)
    texto = "Bolo de chocolate adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)



@bot.message_handler(commands=["2B"])
def bolo_laranja(mensagem):
    soma_conta_cliente(10, 2)
    texto = "Bolo de laranja adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["3B"])
def bolo_amendoim(mensagem):
    soma_conta_cliente(10, 3)
    texto = "Bolo de amendoim adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["4B"])
def bolo_formigueiro(mensagem):
    soma_conta_cliente(13, 4)
    texto = "Bolo formigueiro adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["5B"])
def bolo_limao(mensagem):
    soma_conta_cliente(12, 5)
    texto = "Bolo de limão adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["6B"])
def bolo_fuba(mensagem):
    soma_conta_cliente(17, 6)
    texto = "Bolo de Fubá adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["7B"])
def bolo_fuba_cremoso(mensagem):
    soma_conta_cliente(20, 7)
    texto = "Bolo de Fubá cremoso adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["8B"])
def bolo_fuba_goiabada(mensagem):
    soma_conta_cliente(20, 8)
    texto = "Bolo de fubá com goiabada adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["9B"])
def bolo_mesclado(mensagem):
    soma_conta_cliente(22, 9)
    texto = "Bolo mesclado adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["10B"])
def bolo_prestigio(mensagem):
    soma_conta_cliente(22, 10)
    texto = "Bolo prestígio adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["11B"])
def bolo_leite_ninho(mensagem):
    soma_conta_cliente(35, 11)
    texto = "Bolo de leite ninho adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["12B"])
def bolo_brigadeiro(mensagem):
    soma_conta_cliente(38, 12)
    texto = "Bolo de brigadeiro adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["13B"])
def bolo_nozes(mensagem):
    soma_conta_cliente(40, 13)
    texto = "Bolo de nozes adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["14T"])
def torta_presunto_queijo(mensagem):
    soma_conta_cliente(20, 14)
    texto = "torta de presunto e queijo adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["15T"])
def torta_palmito(mensagem):
    soma_conta_cliente(20, 15)
    texto = "torta de palmito adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["16T"])
def torta_carne_moida(mensagem):
    soma_conta_cliente(20, 16)
    texto = "torta de carne moída adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["17T"])
def torta_frango(mensagem):
    soma_conta_cliente(20, 17)
    texto = "torta de frango adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["18T"])
def torta_frango_requeijao(mensagem):
    soma_conta_cliente(23, 18)
    texto = "torta de frango com requeijão adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["19T"])
def torta_frango_catupiry(mensagem):
    soma_conta_cliente(23, 19)
    texto = "torta de frango com catupiry adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["20T"])
def torta_atum(mensagem):
    soma_conta_cliente(25, 20)
    texto = "torta de atum adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["21T"])
def torta_ninho_oreo(mensagem):
    soma_conta_cliente(30, 21)
    texto = "torta de ninho com oreo adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["22T"])
def torta_ninho_morango(mensagem):
    soma_conta_cliente(30, 22)
    texto = "torta de ninho com morango adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["23T"])
def torta_limao(mensagem):
    soma_conta_cliente(30, 23)
    texto = "torta de limão adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["24T"])
def torta_maracuja(mensagem):
    soma_conta_cliente(30, 24)
    texto = "torta de maracujá adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["25T"])
def torta_morango(mensagem):
    soma_conta_cliente(30, 25)
    texto = "torta de morango adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["26C"])
def cupcake_chocolate(mensagem):
    soma_conta_cliente(10, 26)
    texto = "cupcake de chocolate adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["27C"])
def cupcake_vanilha(mensagem):
    soma_conta_cliente(10, 27)
    texto = "cupcake de vanilha adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["28C"])
def cupcake_maracuja(mensagem):
    soma_conta_cliente(10, 28)
    texto = "cupcake de maracujá adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["29C"])
def cupcake_chocolate_branco(mensagem):
    soma_conta_cliente(10, 29)
    texto = "cupcake de chocolate branco adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["30C"])
def cupcake_morango(mensagem):
    soma_conta_cliente(10, 30)
    texto = "cupcake de morango adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["31C"])
def cupcake_brigadeiro(mensagem):
    soma_conta_cliente(13, 31)
    texto = "cupcake de brigadeiro adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["32C"])
def cupcake_doce_leite(mensagem):
    soma_conta_cliente(13, 32)
    texto = "cupcake de doce de leite adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["33C"])
def cupcake_frutas_vermelhas(mensagem):
    soma_conta_cliente(13, 33)
    texto = "cupcake de frutas vermelhas adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["34C"])
def cupcake_prestigio(mensagem):
    soma_conta_cliente(13, 34)
    texto = "cupcake de prestigio adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["35C"])
def cupcake_ovomaltine(mensagem):
    soma_conta_cliente(16, 35)
    texto = "cupcake de ovomaltine adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["36C"])
def cupcake_redvelvet(mensagem):
    soma_conta_cliente(16, 36)
    texto = "cupcake de redvelvet adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["37C"])
def cupcake_nutella(mensagem):
    soma_conta_cliente(18, 37)
    texto = "cupcake de nutella adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["38C"])
def cupcake_chocolate_belga(mensagem):
    soma_conta_cliente(18, 38)
    texto = "cupcake de chocolate belga adicionado \n deseja mais alguma coisa /sim ou /nao"
    bot.reply_to(mensagem, texto)



@bot.message_handler(commands=["sair"])
def saida_user(mensagem):
    bot.send_message(mensagem.chat.id, "A Cakeflix agradece pelo seu contato, te esperamos em breve!")


@bot.message_handler(commands=["sim"])
def aumentar_pedido(mensagem):
    fazer_pedido(mensagem)


@bot.message_handler(commands=["nao"])
def forma_pagamento(mensagem):
    texto = f"número do pedido {mensagem.id} e o total ficou {valor_cliente} " \
            f"os itens escolhidos foram {pedido}" \
            f" escolha forma de pagamento na entrega \n /maquininha ou /dinheiro"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["maquininha"])
def maquininha_pagamento(mensagem):
    #salvar forma de pagamento no banco
    texto = f"Ficamos felizes pelo seu pedido e já estamos preparando com muito carinho e amor. Lembramos que o pagamento" \
            f" deverá ser feito na entrega junto ao motoboy!" \
            f"Caso queira encerrar o atendimento clique em /sair ou /menu para ir ao menu principal!"
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["dinheiro"])
def dinheiro_pagamento(mensagem):
    # salvar forma de pagamento no banco
    texto = f"Ficamos felizes pelo seu pedido e já estamos preparando com muito carinho e amor. Lembramos que o pagamento" \
            f" deverá ser feito na entrega junto ao motoboy!" \
            f"Caso queira encerrar o atendimento clique em /sair ou /menu para ir ao menu principal!"
    bot.reply_to(mensagem, texto)

def inicia_chat(mensagem):
    texto = f"""
    Olá, seja bem vindo(a) a Cakeflix, me chamo Wall e serei seu atendente virtual!
    Para acessar o menu inicial clique em /menu"""
    bot.reply_to(mensagem, texto)


def executa_responder(mensagem):
    return True


@bot.message_handler(func=executa_responder)
def responder(mensagem):
    try:
        Thread(target=inicia_chat, args=(mensagem,)).start()
    except Exception as e:
        bot.send_message(mensagem, "não entendemos sua mensagem!")
        print(e)


def soma_conta_cliente(valor, id):
    global valor_cliente
    global pedido
    #inclui os ids do itens que o cliente pediu e adiciona na lista
    pedido.append(id)
    valor_cliente += valor
    print(valor_cliente)
    print(pedido)


bot.polling()
