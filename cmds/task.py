import discord
from discord.ext import commands
from core.classes import Cog_Extension
import asyncio

class Task(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    async def interval(self):
        await self.bot.wait_until_ready()
        self.channel = self.bot.get_channel(1261252910747226174)
        while not self.bot.is_closed():
            await self.channel.send("running")
            await asyncio.sleep(5)
        self.bg_task = asyncio.create_task(self.interval())

    @commands.command()
    async def set_channel(self, ctx, ch: int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set channel: {self.channel.mention}')
        
async def setup(bot):
    await bot.add_cog(Task(bot))
