from typing import List, Dict, Callable
from functools import wraps

import discord
from discord.ext.commands.bot import Bot

class Module:
    funcs: List[str] = []
    
    def check_room(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            allow_rooms: List[str] = args[0].allow_rooms
            print(allow_rooms)
            if not allow_rooms or args[1] not in allow_rooms:
                print(f"Not Allowed Room {args[1]}")
                return
            ret = await func(*args, **kwargs)
            return ret

        return wrapper

    def __init__(self, bot: Bot):
        self.bot = bot
        self.funcs = []