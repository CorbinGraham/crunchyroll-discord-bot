# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import darling_utils
import watch_together
import ichigo
import os
import asyncio
import stalk_users

TOKEN = str(os.environ['002TOKEN'])

client = discord.Client()

darling = None;
watched_channel = None;
tts_announce_channel = None;

@client.event
async def on_message(message):
    global darling
    global watched_channel
    global tts_announce_channel

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('$queue'):
        msg = enqueue_episode.add_to_queue(message, message.content.split(" "))
        connected_users = enqueue_episode.find_users(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('$hello'):
        msg = darling_utils.hello(message, darling)
        await client.send_message(message.channel, msg)

    if message.content.startswith('$darling'):
        msg = darling_utils.darling(message, darling)
        await client.send_message(message.channel, msg)

    if message.content.startswith('$setdarling'):
        msg_hash = darling_utils.set_darling(message)
        msg = msg_hash['msg']
        darling = msg_hash['user']
        await client.send_message(message.channel, msg)

    if message.content.startswith('$watch'):
        msg = watch_together.add_to_queue(message, message.content.split(" "))
        connected_users = watch_together.find_users(message)

        await client.send_message(message.channel, msg)
        if msg == 'BAKA! I need something to enqueue!':
            return

        msg = watch_together.send_ready_message()
        ready_message = await client.send_message(message.channel, msg)
        await client.add_reaction(ready_message, "✅")

        ready = 0
        while(ready < connected_users):
            await client.wait_for_reaction("✅")
            print ('user readied!')
            ready += 1

        await client.send_message(message.channel, '3, 2, 1, Start!', tts=True)

    if message.content.startswith('$ichigo'):
        msg = ichigo.ichigo()
        await client.send_message(message.channel, msg)

    if message.content.startswith('$usernotifications'):
        msg = stalk_users.enable(message)
        tts_announce_channel = message.channel
        watched_channel = message.author.voice.voice_channel
        await client.send_message(message.channel, msg)

@client.event
async def on_voice_state_update(before, after):
    if watched_channel != None:
        if (before.voice_channel != watched_channel) and (after.voice_channel == watched_channel):
            await client.send_message(tts_announce_channel, after.name + ' has joined channel', tts = True)

        elif (before.voice_channel == watched_channel) and (after.voice_channel != watched_channel):
            await client.send_message(tts_announce_channel, after.name + ' has left channel', tts = True)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
