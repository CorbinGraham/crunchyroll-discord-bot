# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import os

TOKEN = str(os.environ['002TOKEN'])

client = discord.Client()

darling = None;

@client.event
async def on_message(message):
    global darling

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        if (darling != None) and (message.author.name == darling.name):
            msg = 'Hello darling!'.format(message)
        else:
            msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!darling'):
        if darling == None:
            msg = 'I have no darling...'.format(message)
        else:
            msg = darling.mention + ' is my darling!'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!setdarling'):
        args = message.content.split(" ")
        try:
            user = message.server.get_member_named(args[1])
        except Exception as IndexError:
            user = None

        if (user == None):
            msg = 'Where\'s my darling?'.format(message)
        else:
            darling = user
            msg = darling.mention + ' is my new darling!'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
