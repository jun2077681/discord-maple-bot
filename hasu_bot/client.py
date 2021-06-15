from typing import Dict, List

import discord
from discord.ext.commands.bot import Bot

from hasu_bot.modules import Module

from hasu_bot.modules.hilla_timer import HillaTimerModule

class InvalidTokenError(Exception):
    def __init__(self, expression):
        super().__init__(f'잘못된 Bot Token "{expression}"입니다.')

class HasuBot(Bot):
    modules: Dict[str, List[Module]] = {}

    def __init__(self, token, command_prefix = "!"):
        super().__init__(command_prefix = command_prefix)
        self.command_prefix = command_prefix
        if not token:
            raise InvalidTokenError(token)
        self.modules['maple'] = [HillaTimerModule]
        self.set_commands()

        self.run(token)
    
    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("==========")
        await self.change_presence(activity=discord.Game(name="야옹", type=1))
    
    def set_commands(self):
        for server in self.modules:
            for module in self.modules[server]:
                for func in module.funcs:
                    setattr(module, func, self.command()(getattr(module, func)))