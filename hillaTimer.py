import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from gtts import gTTS
import os
import asyncio
import datetime

class TTSEngin:
    def __init__(self, lang = 'ko'):
        self.lang = lang

    async def gen_text_to_mp3(self, text, filename = 'time.mp3'):
        if os.path.isfile(filename):
            os.remove(filename)

        tts = gTTS(text = text, lang = self.lang, slow=False)
        
        return tts

class HillaTimer:
    def __init__(self, vc: discord.voice_client.VoiceClient):
        self.time = 60 * 30
        self.next_time = 29 * 60 + 20
        self.TTS = TTSEngin()
        self.vc = vc
        self.phase = 1

        for i in os.listdir():
            if i.endswith('.mp3'):
                os.remove(i)
        
        print(f"START: {datetime.datetime.now()}")

    def decrease_time(self):
        self.time -= 1

    def set_time(self, minutes, seconds):
        self.time = minutes * 60 + seconds

    def set_phase(self, phase):
        self.phase = phase

    async def check_time_range(self, range_list: list):
        for r in range_list:
            if self.next_time + r == self.time:
                print(f"{r}초 후 낫베기 {datetime.datetime.now()}")
                await self.TTS.gen_text_to_mp3(f"{r}초 후 낫베기", 'time.mp3')
                try:
                    await self.vc.play(FFmpegPCMAudio(source="time.mp3"), after=lambda e: print('done', e))
                except:
                    pass

    async def calc_next_time(self, ctx: commands.context.Context):
        if self.phase == 1:
            self.next_time -= 150
        elif self.phase == 2:
            self.next_time -= 125
        elif self.phase == 3:
            self.next_time -= 100
        
        await ctx.send(f"다음 낫베기: {self.next_time // 60}분 {self.next_time % 60}초")

        print(f"다음 낫베기: {self.next_time // 60}분 {self.next_time % 60}초 {datetime.datetime.now()}")
        await self.TTS.gen_text_to_mp3(f"{self.next_time // 60}분 {self.next_time % 60}초", 'next_time.mp3')
        try:
            await self.vc.play(FFmpegPCMAudio(source="next_time.mp3"), after=lambda e: print('done', e))        
        except:
            pass

    async def start_timer(self, ctx: commands.context.Context):
        self.decrease_time()
        if self.time % 10 == 0:
            remain_time = self.time - self.next_time
            print(f'남은 시간: {remain_time // 60}분 {str(remain_time % 60).zfill(2)}초 ({remain_time}초) {datetime.datetime.now()}')
            await ctx.send(f'남은 시간: {remain_time // 60}분 {str(remain_time % 60).zfill(2)}초 ({remain_time}초)')
        await self.check_time_range([10, 30, 60])

        if self.time <= self.next_time:
            await self.calc_next_time(ctx)
        
        await self.TTS.gen_text_to_mp3(f"{self.time // 60}분 {self.time % 60}초")