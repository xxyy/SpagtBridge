import hexchat

__module_name__ = "Spagt Bridge"
__module_version__ = "0.1-AWSUM"
__module_description__ = "Changes how SpagtBridge's messages are displayed"

def chanmessage(word, word_eol, userdata, attr):
	nick = word[0]
	message = word[1]
	if (hexchat.nickcmp(hexchat.strip(nick), "S") == 0 or hexchat.nickcmp(hexchat.strip(nick), "SpagtBridge") == 0) and message.startswith("<"):		
		name = message[1:message.index('>')] + ":"
		message = message[message.index('>') + 2:]
		mode = name[1] if name[1] in "@+&~%" else ""
		name = name if mode == "" else name[2:]

		hexchat.emit_print(userdata, name, message, mode, time = attr.time)
		return hexchat.EAT_ALL
	return hexchat.EAT_NONE

hexchat.hook_print_attrs("Channel Message", chanmessage, "Channel Message")
hexchat.hook_print_attrs("Channel Msg Hilight", chanmessage, "Channel Msg Hilight")
hexchat.hook_print_attrs("Channel Action", chanmessage, "Channel Action")
hexchat.hook_print_attrs("Channel Action Hilight", chanmessage, "Channel Action Hilight")
