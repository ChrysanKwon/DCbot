# 導入Discord.py模組
import discord
# 導入commands指令模組
from discord.ext import commands
from core.classes import Cog_Extension
 
class Event(Cog_Extension):
    # 讀取event
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel= self.bot.get_channel(1261252910747226174)
        await channel.send(f'{member} join!')
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel= self.bot.get_channel(1261252910747226174)
        await channel.send(f'{member} leave!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content=='apple' and msg.author != self.bot.user:
            await msg.channel.send('hi')

async def setup(bot):
    await bot.add_cog(Event(bot))