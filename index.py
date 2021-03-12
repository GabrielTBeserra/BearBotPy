import discord

from core import database
from os import listdir
from discord.ext import commands

default_prefixes = '.'
custom_prefixes = {}

# Funcao para acessar os comandos de acordo com o prefix do servidor que esta solicitando


async def determine_prefix(bot, message):
    return bot.database.read_out(message.guild.id)['prefix']

# Definicao das variavis
bot = commands.Bot(command_prefix=determine_prefix, case_insensitive=True)
bot.database = database.Database()


@bot.event
async def on_ready():
    print('Bot logado usando a tag: {0.user}'.format(bot))
    if __name__ == "__main__":
        for fou in listdir('./commands/'):
            for cmd in listdir(f'./commands/{fou}'):
                if cmd.endswith('.py'):
                    print(f"Carregando o comando {cmd.split('.')[0]}")
                    try:
                        bot.load_extension(
                            f'commands.{fou}.{cmd.split(".")[0]}')
                        print(f"Comando {cmd.split('.')[0]} carregado! ✅")
                    except Exception as exce:
                        print(
                            f"Oopsie Woopsie, you made a fucky wucky!\nFalha no carregamento do comando {type(exce).__name__}!\n{exce} ❌")

bot.run('')
