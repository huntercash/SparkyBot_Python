import discord
import asyncio
import aiohttp
import random
from discord import Game
from discord.ext.commands import Bot
from Token import TOKEN_REF

BOT_PREFIX = ("_","-")

TOKEN = TOKEN_REF

client = Bot(command_prefix=BOT_PREFIX)


# 8 Ball Thing
@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

#Telling the bot _hi and having it reply
@client.command(name='hi',
                description="Tells the user hi using various movie quotes",
                brief="Hey Man.",
                aliases=['hey', 'sup', 'hello', 'yo'],
                pass_context=True)
async def hi_there(context):
    hithere_responses = [
        "Hey, man. I'm Korg. This is " + context.message.author.mention + " We're gonna jump on that spaceship and get outta here. Wanna come?",
        "What's up " + context.message.author.mention,
        context.message.author.mention + " was here",
    ]
    await client.say(random.choice(hithere_responses))



#Displays a message under the bots username in the discord channel as "playing ####"
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="MacBot 0.1"))
    print("Logged in as " + client.user.name)
    print(client.user.id)
    print(client.user.name)
    print('------')
    

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)