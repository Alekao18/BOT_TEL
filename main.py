def verificacao(mensagem):
    # Aqui você pode implementar qualquer lógica para filtrar mensagens
    return True  # O bot irá responder a qualquer mensagem

def resposta(mensagem, bot):
    bot.reply_to(mensagem, 'Olá, eu sou o Leko')  # Usa bot.reply_to corretamente
    texto = """ 
     Digite 1 para fazer um pedido
    Digite 2 para reclamar de um pedido
    Digite 3 para encerrar
    """
    bot.reply_to(mensagem, texto)  # Usa bot.reply_to corretamente


