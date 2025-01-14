import telebot #biblioteca do telegrambot

link_bot = 't.me/Lekaobot_bot.'
KEY_API = '7642544580:AAFA_KXDWgP7jJukIg7WLiMYnJtQw8NsZMQ' #chave API

bot = telebot.TeleBot(KEY_API)
#conexão feita com o bot criado no telegram

@bot.message_handler(commands=["1"]) #parametro que gera um comando ou função para a minha função rodar
def digite1(mensagem):
    bot.reply_to(mensagem, 'Obrigado por escolher nossa empresa!')
    texto = """ 
    Seja bem vindo ao nosso site!</b>
    Escolha um de nossos serviços para continuar:
        /formatacao 
        /limpeza
        /instalcaodrivers 
        /completo
        /fazerorcamento
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["2"])
def digite2(mensagem):
    reclamacao = bot.reply_to(mensagem, 'Digite aqui a sua reclamação:')
    bot.register_next_step_handler(reclamacao, armazenar_reclamacao)

def armazenar_reclamacao(mensagem): 
    bot.send_message(mensagem.chat.id, 'Muito obrigado por nos informar, não haverá mais isso')

@bot.message_handler(commands=["3"])
def digite3(mensagem):
    bot.send_message(mensagem.chat.id, 'Sessão encerrada')

def verificacao(mensagem):
    return True #bot ira responder a qualquer mensagem
#função que irá verificar se o usuario der inicio com o comando correto

@bot.message_handler(func=verificacao) #parametro que gera um comando ou função para a minha função rodar
def reposta(mensagem):
    bot.reply_to(mensagem, 'Ola, eu sou o Leko')
    texto = """ 
     Digite 1 para fazer um pedido
    Digite 2 para reclamar de um pedido
    Digite 3 para encerrar
    """
    bot.reply_to(mensagem, texto) #mensagem padrão(teste)
#função para testar as respotas de mensagem do usuário

bot.polling() #comando que permite a leitura de todas as mensagens recebidas pelo bot