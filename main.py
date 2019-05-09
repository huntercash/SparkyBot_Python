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

# I am always right
@client.command(name="youareright",
                pass_context=True)
async def you_are_right(context):
  await client.say("It is Known")

# No
@client.command(name='thirdbranch',
                description="emoji?",
                brief="bad bad bad",
                aliases=['please', 'illinois', 'no'],
                pass_context=True)
async def emoji_squirt(context):
    squirt_emoji_reponse = "<:squirt:575768643850469386>"
    await client.say(squirt_emoji_reponse)


#Allies and NAPS
@client.command(name='naps',
                description="300 Allies and Naps",
                brief="300's Allies and Naps",
                aliases=['war', 'enemies', 'allies'],
                pass_context=True)
async def allies_naps(context):
    allies = """
Seriously? How could you forget?!
Current Allies: None
Naps:
03APR2019: VIPER/VENOM
19APR2019: OXIA
21APR2019: BINDA
- If you attack any of these not during pvp I will punt you                
- Viper/Venom: Can attack and take SOPS only during pvp"""
    await client.say(allies)

#White Flag Response
@client.command(name='whiteflag',
                description="should you get a whiteflag",
                brief="hmmmm maybe",
                pass_context=True)
async def white_flag_function(context):
    white_flag_response = ["Bitch, you better not be on a honeymoon",
                           "Livia is the boss",
                           ]
    await client.say(random.choice(white_flag_response))

#because i said so 
@client.command(name='howdidthathappen',
                aliases=['why'],
                pass_context=True)
async def saidso_function(context):
    because_respone = "Sparky said so <:squirt:575768643850469386>"
    await client.say(because_respone)


@client.command(name='schedule',
                pass_context=True)
async def schedule_function(context):
    spark_schedule = """
Spart has the following schedule
TimeZone CST (-6)
Monday - Work 9-5, Class 6:30-9:30
Tuesday - Work 9-5:30
Wednesday - Work 9-5, Class 6:30-9:30
Thursday - Work 9-5:30 (work from home)
Friday - Work 9-5:30
Saturday - Class 10:00-2:00
Sunday - Nothingggg
"""
    await client.say(spark_schedule)


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