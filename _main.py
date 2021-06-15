import discord
from discord.ext import commands
from config.config import token as secret_token
from hasu_bot import HasuBot

if __name__ == "__main__":
    try:
        client = HasuBot(secret_token, command_prefix="!")
        #client.run()
    except Exception as e:
        print(e)