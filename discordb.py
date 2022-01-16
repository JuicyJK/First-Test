import os
import discord 
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='-')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    await client.process_commands(message)
    await message.channel.send('test')


@client.command()
async def repeatmessage(message):
    await message.channel.send("for")



client.run(TOKEN)
