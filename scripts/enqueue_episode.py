def add_to_queue(message, split_command):
	try:
	  msg = message.author.mention + ' has enqueued ' + split_command[1].format(message)
	except IndexError:
	  msg = 'BAKA! I need something to enqueue!'
	return msg