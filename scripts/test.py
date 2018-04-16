# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import enqueue_episode

TOKEN = 'NDM1MTk1MjMxMjA2NjM3NTk5.DbVcSQ.HLl5aMpe8G-ystPZtrfozhBIoIY'

client = discord.Client()

@client.event
async def on_message(message):
    # import pdb; pdb.set_trace()
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!queue'):
        msg = enqueue_episode.add_to_queue(message, message.content.split(" "))
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)