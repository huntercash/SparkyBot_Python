import discord
import os
import asyncio
import random
from discord.ext.commands import Bot
from auth import token

BOT_PREFIX = ("_","-","!")
client = Bot(command_prefix=BOT_PREFIX)

#8 Ball
@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'i cant say no',
        'idk, but Airis is my #1 wife',
        'idk, but im going down the street to have a mimosa',
        'It is known',
        'Sparky said I was right. I pinned it in discord',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

#Say hello
@client.command(name='hi',
                description="Things athena says",
                brief="don't upgrade my firmware",
                aliases=['hey', 'sup', 'hello', 'yo'],
                pass_context=True)
async def hi_there(context):
    hithere_responses = ["What do you mean you didn't read the rein channel " + context.message.author.mention + " You're being kicked!",
                         "I can't find my pants, can you help me " + context.message.author.mention + "?",
    ]
    await client.say(random.choice(hithere_responses))

@client.command(name="youareright",
                pass_context=True)
async def you_are_right(context):
  await client.say("It is Known")






#---------------------------------------End-----------------------
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Firmware 1.0"))
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

client.run(token)