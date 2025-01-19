import os
from dotenv import load_dotenv
load_dotenv()

import telebot #biblioteca do telegrambot

link_bot = 't.me/Lekaobot_bot.'
TEL_API = os.getenv('KEY_API') #chave API

bot = telebot.TeleBot(TEL_API)
#conexão feita com o bot criado no telegram

@bot.message_handler(commands=["1"]) #parametro que gera um comando ou função para a minha função rodar
def digite1(mensagem):
    bot.reply_to(mensagem, 'Obrigado por escolher nossa empresa!')
    texto = """ 
    Seja bem vindo ao nosso site!
    Escolha um de nossos serviços para continuar:
        /formatacao 
        /limpeza
        /instalacaodrivers 
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

@bot.message_handler(commands=["formatacao"])
def formatacao(mensagem):
    bot.reply_to(mensagem, 'A formatação fica R$50,00')

@bot.message_handler(commands=["limpeza"])
def limpeza(mensagem):
    bot.reply_to(mensagem, 'A limpeza fica R$20,00')

@bot.message_handler(commands=["instalacaodrivers"])
def instalacaodrivers(mensagem):
    bot.reply_to(mensagem, 'A instalação de drivers fica R$35,00')

@bot.message_handler(commands=["completo"])
def completo(mensagem):
    bot.reply_to(mensagem, 'O serviço completo fica R$110,00')

@bot.message_handler(commands=["fazerorcamento"])
def fazerorcamento(mensagem):
    bot.reply_to(mensagem, 'Aguarde para fazer o orçamento com um atendente!')

def verificacao(mensagem):
    # Aqui você pode implementar qualquer lógica para filtrar mensagens
    return True  # O bot irá responder a qualquer mensagem

@bot.message_handler(func=verificacao)
def resposta(mensagem):
    bot.reply_to(mensagem, 'Olá, eu sou o Leko')  # Usa bot.reply_to corretamente
    texto = """ 
     Digite 1 para fazer um pedido
    Digite 2 para reclamar de um pedido
    Digite 3 para encerrar
    """
    bot.reply_to(mensagem, texto)  # Usa bot.reply_to corretamente

bot.polling() #comando que permite a leitura de todas as mensagens recebidas pelo bot