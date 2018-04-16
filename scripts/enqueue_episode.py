def build_message(message, split_command):
	try:
	  msg = message.author.mention + ' has enqueued ' + split_command[1].format(message)
	except IndexError:
	  msg = 'BAKA! I need something to enqueue!'
	return msg

def add_to_queue(message, split_command):
	return find_caller(message)

def find_caller(message):
	caller = message.author.voice.voice_channel
	if caller:
		find_users(message)
	else:
		return 'You need to be in a channel'

# def find_users(message):