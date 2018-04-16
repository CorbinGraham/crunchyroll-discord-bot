# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import watch_together
import os
import asyncio

TOKEN =  str(os.environ['002TOKEN'])

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('$watch'):
        msg = watch_together.add_to_queue(message, message.content.split(" "))
        connected_users = watch_together.find_users(message)

        await client.send_message(message.channel, msg)

        msg = watch_together.send_ready_message()
        ready_message = await client.send_message(message.channel, msg)
        await client.add_reaction(ready_message, "✅")

        ready = 0
        while(ready < connected_users):
            await client.wait_for_reaction("✅")
            print ('user readied!')
            ready += 1

        await client.send_message(message.channel, '3, 2, 1, Start!', tts=True)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
