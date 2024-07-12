# 導入Discord.py模組
import discord
# 導入commands指令模組
from discord.ext import commands
from core.classes import Cog_Extension

class React(Cog_Extension):
    @commands.command()
    async def pic(self, ctx):
        await ctx.send(file=discord.File('E:\\DCbot\\pic\\pandora.jpg'))

async def setup(bot):
    await bot.add_cog(React(bot))