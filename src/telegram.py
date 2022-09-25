from cgitb import text
import numbers
from re import M
from socket import NI_NUMERICHOST
from typing import Text
import telebot

CHAVE_API = "5668253553:AAFk8c8x9KjxrCJTBX_x-JM9jK_gjWe3_MM"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands= ["sim"]) ## Agendar Sinal
def sim(mensagem):
    bot.reply_to(mensagem, "Agendado.")

    
@bot.message_handler(commands= ["R10"]) ## Agendar Sinal
def R10(mensagem):
    print(mensagem)
    bot.reply_to(mensagem, """Confirmar agendamento:
    /sim
    /nao
    """)

@bot.message_handler(commands= ["R20"]) ## Agendar Sinal
def R20(mensagem):
    print(mensagem)
    bot.reply_to(mensagem, """Confirmar agendamento:
    /sim
    /nao
    """)

@bot.message_handler(commands= ["R30"]) ## Agendar Sinal
def R30(mensagem):
    print(mensagem)
    bot.reply_to(mensagem,  """Confirmar agendamento:
    /sim
    /nao
    """)

@bot.message_handler(commands= ["R40"]) ## Agendar Sinal
def R40(mensagem):
    print(mensagem)
    bot.reply_to(mensagem,  """Confirmar agendamento:
    /sim
    /nao
    """)

@bot.message_handler(commands= ["R50"]) ## Agendar Sinal
def R50(mensagem):
    print(mensagem)
    bot.reply_to(mensagem,  """Confirmar agendamento:
    /sim
    /nao
    """)

@bot.message_handler(commands= ["R60"]) ## Agendar Sinal
def R60(mensagem):
    print(mensagem)
    bot.reply_to(mensagem,  """Confirmar agendamento:
    /sim
    /nao
    """)

@bot.message_handler(commands= ["R70"]) ## Agendar Sinal
def R70(mensagem):
    print(mensagem)
    bot.reply_to(mensagem,  """Confirmar agendamento:
    /sim
    /nao
    """)

@bot.message_handler(commands= ["R80"]) ## Agendar Sinal
def R80(mensagem):
    print(mensagem)
    bot.reply_to(mensagem,  """Confirmar agendamento:
    /sim
    /nao
    """)

@bot.message_handler(commands= ["R90"]) ## Agendar Sinal
def R90(mensagem):
    print(mensagem)
    bot.reply_to(mensagem,  """Confirmar agendamento:
    /sim
    /nao
    """)

@bot.message_handler(commands= ["R100"]) ## Agendar Sinal
def R100(mensagem):
    print(mensagem)
    bot.reply_to(mensagem,  """Confirmar agendamento:
    /sim
    /nao
    """)



@bot.message_handler(commands=["S1"]) ## Inscrição Grupo Free
def S1(mensagem):
    bot.reply_to(mensagem, "Acesse o link e faça sua inscrição:")

@bot.message_handler(commands=["S2"]) ## Inscrição Grupo Vip
def S2(mensagem):
    bot.reply_to(mensagem, "Acesse o link e faça sua inscrição:")

@bot.message_handler(commands=["S3"]) ## Agendar Sinal
def S3(mensagem):
    bot.reply_to(mensagem, """
    Quantia de entrada:
    /R10
    /R20
    /R30
    /R40
    /R50
    /R60
    /R70
    /R80
    /R90
    /R100
    R = Reais
    Atenção! Se não for inscrito, não irá ser agendado.
    """)





def verificar(mensagem):
	return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Olá, seja bem-vindo ao Sinais IQOption.
    
    Clique e escolha uma de nossas opções:
    /S1 - Inscrição Grupo Free
    /S2 - Inscrição Grupo Vip
    /S3 - Agendar Sinal"""
    bot.reply_to(mensagem, texto)



bot.polling()