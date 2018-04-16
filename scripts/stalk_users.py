def enable (message):
    voice_channel = message.author.voice.voice_channel
    if voice_channel == None:
        return 'You must be in a voice channel!'
    else:
        return 'Notifications enabled on ' + voice_channel.mention
