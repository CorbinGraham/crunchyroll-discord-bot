def darling(message, darling):
    if darling == None:
        msg = 'I have no darling...'.format(message)
    else:
        msg = darling.mention + ' is my darling!'.format(message)
    return msg

def set_darling(message):
    args = message.content.split(" ")
    message_user_values = {}
    try:
        message_user_values["user"] = message.server.get_member_named(args[1])
    except Exception as IndexError:
        message_user_values["user"] = None

    if (message_user_values["user"] == None):
        message_user_values["msg"] = 'Where\'s my darling?'.format(message)
    else:
        message_user_values["msg"] = message_user_values["user"].mention + ' is my new darling!'.format(message)
    return message_user_values

def hello(message, darling):
    if (darling != None) and (message.author.name == darling.name):
        msg = 'Hello darling!'.format(message)
    else:
        msg = 'Hello {0.author.mention}'.format(message)
    return msg