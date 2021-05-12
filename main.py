import discord
from discord.ext import commands, tasks
from config.config import token as secret_token
import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from hillaTimer import HillaTimer

bot = commands.Bot(command_prefix = '!')
scheduler = AsyncIOScheduler()

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("==========")
    await bot.change_presence(activity=discord.Game(name="야옹", type=1))

@bot.command()
async def 종료(ctx: commands.context.Context):
    print("Logout")
    await bot.logout()

@bot.command()
async def 진힐라(ctx: commands.context.Context, command: str = ''):
    if command == '종료':
        scheduler.shutdown()
        scheduler.remove_all_jobs()
    elif command == '시작':
        hilla_timer = HillaTimer()
        scheduler.add_job(hilla_timer.start_timer, 'interval', seconds = 1, id = 'hilla_timer', args=(ctx, ))
        scheduler.start()
    elif command == '1':
        return
    elif command == '2':
        return
    elif command == '3':
        return

bot.run(secret_token)