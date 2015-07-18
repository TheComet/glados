from willie import module

phrases = [
	"You need to shut up, {0}"
]
counter = 0

@module.rule("^.*(shut)(up)(glados).*$")
def shut_up(bot, trigger):
	global phrases
	global counter
	bot.say(phrases[counter].format(trigger.nick))
	counter = (counter + 1) % len(phrases)
