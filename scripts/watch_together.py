def add_to_queue(message, split_command):
	return find_caller(message, split_command)

def find_caller(message, split_command):
	caller = message.author.voice.voice_channel
	if caller:
		return build_message(message, split_command)
	else:
		return 'You need to be in a voice channel!'

def build_message(message, split_command):
	try:
	  msg = message.author.mention + ' wants to watch ' + split_command[1].format(message)
	except IndexError:
	  msg = 'BAKA! I need something to enqueue!'
	return msg

def find_users(message):
	counter = 0
	users = message.author.voice.voice_channel.voice_members

	for User in users:
		if User.bot == False:
			counter += 1

	return counter

def send_ready_message():
	return "Click the check when you're ready to watch!"
