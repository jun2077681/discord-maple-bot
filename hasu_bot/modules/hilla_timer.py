from typing import List, Dict, Callable
from hasu_bot.modules import Module
from discord.ext import commands
from discord.ext.commands.bot import Bot

class HillaTimerModule(Module):
    funcs: List[str] = ['인사']
    allow_rooms = []

    def __init__(self, bot: Bot):
        self.bot = bot

    @classmethod
    @Module.check_room
    async def 인사(cls, ctx: commands.context.Context):
        await ctx.send("HI")