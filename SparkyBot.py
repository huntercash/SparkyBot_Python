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

#Test Reply Stuff
#@client.event
#async def on_message(message):
#    # we do not want the bot to reply to itself
#    if message.author == client.user:
#        return
#
#    if message.content.startswith('_hello'):
#        msg = 'Hello {0.author.mention}'.format(message)
#        await client.send_message(message.channel, msg)
#
#    if message.content.startswith('_mad'):
#        msg = "I'm Going To Build My Own Bot With Blackjack and Hookers".format(message)
#        await client.send_message(message.channel, msg)


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



@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Macbot 2.0"))
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