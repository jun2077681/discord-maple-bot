import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from config.config import token as secret_token
import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from hillaTimer import HillaTimer

bot = commands.Bot(command_prefix = '!')
scheduler = AsyncIOScheduler()
hilla_timer: HillaTimer = None
vc: discord.voice_client.VoiceClient = None

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
async def 진힐라(ctx: commands.context.Context, command: str = '시작'):
    print(f"command: {command}")
    
    global hilla_timer
    global vc
    
    if command == '종료':
        scheduler.shutdown()
        scheduler.remove_all_jobs()
        hilla_timer = None
        if vc:
            await vc.disconnect()
    elif command == '시작':
        try:
            if ctx.author.voice:
                vc = await ctx.author.voice.channel.connect()
            else:
                raise AttributeError
        except AttributeError:
            await ctx.send("음성채널 연결을 확인하세요.")
            return

        if hilla_timer == None:
            hilla_timer = HillaTimer(vc)
        scheduler.add_job(hilla_timer.start_timer, 'interval', seconds = 1, id = 'hilla_timer', args=(ctx, ))
        scheduler.start()
    elif command == '1':
        hilla_timer.set_phase(1)
        return
    elif command == '2':
        hilla_timer.set_phase(2)
        return
    elif command == '3':
        hilla_timer.set_phase(3)
        return

@bot.command()
async def 테스트(ctx: commands.context.Context):
    vc: discord.voice_client.VoiceClient = await ctx.author.voice.channel.connect()
    
    hilla_timer = HillaTimer(vc)
    hilla_timer.TTS.gen_text_to_mp3(f"{r}초 후 낫베기", 'time.mp3')

    vc.play(FFmpegPCMAudio(source='hello.mp3'), after=lambda e: print('done', e))

bot.run(secret_token)