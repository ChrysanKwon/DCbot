# 導入Discord.py模組
import discord
# 導入commands指令模組
from discord.ext import commands
import json
import os
import asyncio

# intents是要求機器人的權限
intents = discord.Intents.all()
# command_prefix是前綴符號，可以自由選擇($, #, &...)
bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")


#cog讀取函式
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f'cmds.{extension}')
@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f'cmds.{extension}')
@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f'cmds.{extension}')

#讀取全部cmds
async def load_cmds():
    for filename in os.listdir('cmds'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cmds.{filename[:-3]}')

#讀取設定
with open('token.json','r') as tokenfile:
    token = json.load(tokenfile)

# main
async def main():
    await load_cmds()
    await bot.start(token['token'])


if __name__ == "__main__":
    asyncio.run(main())

'''
json可包含
token
channelid

'''