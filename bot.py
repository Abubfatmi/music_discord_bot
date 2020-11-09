import discord,asyncio,youtube_dl
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()




def get_prefix(bot, msg):
    

    prefixes = ['.'] 

    return commands.when_mentioned_or(*prefixes)(bot, msg)

bot=commands.Bot(command_prefix=get_prefix,description='Multipurpose Discord Bot')




exts=['music'] 


@bot.event
async def on_ready():
    song_name='with All For One' 
    activity_type=discord.ActivityType.playing
    await bot.change_presence(activity=discord.Activity(type=activity_type,name=song_name))
    print(bot.user.name)






for i in exts:
    bot.load_extension(i)


bot.run('NzU5MTAzMjExMDA4Njg4MTM5.X24n9A.Mkj6rqO7l1sR1JkBkwZ2qVpfM7s')