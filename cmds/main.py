# 導入Discord.py模組
import discord
# 導入commands指令模組
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import random

def color():
    return random.randint(0, 0xFFFFFF)
    

class Main(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(self.bot.latency)

    @commands.command()
    # 輸入!Hello呼叫指令
    async def Hello(self, ctx):
        # 回覆Hello, world!
        await ctx.send("Hello, world!")
    
    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="about", color=color(), timestamp=datetime.datetime.now())
        embed.set_author(name=ctx.message.author.name)
        embed.add_field(name="1", value="2", inline=False)
        embed.add_field(name="3", value="4", inline=False)
        embed.add_field(name="5", value="6", inline=False)
        embed.set_footer(text="aaa")
        await ctx.send(embed=embed)

    #訊息複誦
    @commands.command()
    async def sayd(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    
    #訊息清理
    @commands.command()
    async def clean(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)

async def setup(bot):
    await bot.add_cog(Main(bot))