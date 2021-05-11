import discord
from discord.ext import commands, tasks
from config.config import token as secret_token
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from hillaTimer import HillaTimer

bot = commands.Bot(command_prefix = '!')
scheduler = BackgroundScheduler()

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("==========")
    await bot.change_presence(activity=discord.Game(name="야옹", type=1))

@bot.command()
async def 종료(ctx):
    print("Logout")
    await bot.logout()

@bot.command()
async def 진힐라(ctx):

    
bot.run(secret_token)