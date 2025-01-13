import telebot #biblioteca do telegrambot

link_bot = 't.me/Lekaobot_bot.'
KEY_API = '7642544580:AAFA_KXDWgP7jJukIg7WLiMYnJtQw8NsZMQ' #chave API

bot = telebot.TeleBot(KEY_API)
#conexão feita com o bot criado no telegram

def verificacao(mensagem):
    return True #bot ira responder a qualquer mensagem
#função que irá verificar se o usuario der inicio com o comando correto

@bot.message_handler(func=verificacao) #parametro que gera um comando ou função para a minha função rodar
def reposta(mensagem):
    bot.reply_to(mensagem, "Olá, aqui é o LekoBot!") #mensagem padrão(teste)
    texto = '''
    Digite 1 para fazer um pedido
    Digite 2 para reclamar de um pedido
    Digite 3 para encerrar
    '''
    bot.reply_to(texto)
    if texto =='1':
        bot.reply_to(mensagem,'Obrigado por escolher nossa empresa')
    elif texto == '2':
        reclamacao = bot.reply_to(mensagem,'Descreva aqui para nós o motivo de sua reclamação')
        bot.reply_to(mensagem, reclamacao, 'Certo, pedimos perdão pelo transtorno e iremos informar assim que sair a procuração!')
    else:
        bot.reply_to(mensagem,'Volte sempre.')
#função para testar as respotas de mensagem do usuário


bot.polling() #comando que permite a leitura de todas as mensagens recebidas pelo bot