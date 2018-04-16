def add_to_queue(message, split_command):
	return find_caller(message, split_command)

def find_caller(message, split_command):
	caller = message.author.voice.voice_channel
	if caller:
		return build_message(message, split_command)
	else:
		return 'You need to be in a channel'

def build_message(message, split_command):
	try:
	  msg = message.author.mention + ' has enqueued ' + split_command[1].format(message)
	except IndexError:
	  msg = 'BAKA! I need something to enqueue!'
	return msg

def find_users(message):
	message.author.voice.voice_channel.voice_members